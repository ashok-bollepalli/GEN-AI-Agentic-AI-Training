import torch
import torch.nn as nn
from torch.nn import functional as F


# ============================================================
# 1. SIMPLE TRAINING DATA
# ============================================================

training_text = """
python is easy to learn.
python is useful for artificial intelligence.
python is used for data science.
java is used for enterprise applications.
java supports object oriented programming.
langchain helps us build llm applications.
langgraph helps us build ai workflows.
crewai helps us build multi agent applications.
rag helps llms answer using external documents.
fastapi helps us build rest apis using python.
"""

# ============================================================
# 2. CREATE CHARACTER VOCABULARY
# ============================================================

characters  = sorted(list(set(training_text)))
vocab_size = len(characters)
print("Characters : ")
print(characters)

print("\nVocabulary Size:")

print(vocab_size)


# ============================================================
# 3. CHARACTER TO NUMBER MAPPING
# ============================================================

char_to_id = {
    character: index
    for index, character in enumerate(characters)
}

id_to_char = {
    index: character
    for index, character in enumerate(characters)
}

# ============================================================
# 4. ENCODE AND DECODE FUNCTIONS
# ============================================================


def encode(text):

    return [
        char_to_id[character]
        for character in text
    ]


def decode(token_ids):

    return "".join(
        id_to_char[token_id]
        for token_id in token_ids
    )

# Convert training text into numbers

data = torch.tensor(
    encode(training_text),
    dtype=torch.long,
)

print("\nEncoded Data:")
print(data)

print("\nDecoded Data:")
print(decode(data.tolist()))

# ============================================================
# 5. TRAINING SETTINGS
# ============================================================

block_size = 20

batch_size = 16

embedding_size = 64

learning_rate = 0.01

training_steps = 3000

# ============================================================
# 6. CREATE TRAINING BATCH
# ============================================================

def get_batch():

    starting_positions = torch.randint(
        0,
        len(data) - block_size - 1,
        (batch_size,),
    )


    inputs = torch.stack(
        [
            data[position:position + block_size]
            for position in starting_positions
        ]
    )


    targets = torch.stack(
        [
            data[position + 1:position + block_size + 1]
            for position in starting_positions
        ]
    )


    return inputs, targets


# ============================================================
# 7. CREATE SMALL LANGUAGE MODEL
# ============================================================

class TinyLanguageModel(nn.Module):

    def __init__(self):

        super().__init__()


        self.embedding = nn.Embedding(
            vocab_size,
            embedding_size,
        )


        self.hidden_layer = nn.Linear(
            embedding_size,
            embedding_size,
        )


        self.output_layer = nn.Linear(
            embedding_size,
            vocab_size,
        )


    def forward(self, inputs, targets=None):

        embeddings = self.embedding(inputs)


        hidden_output = torch.relu(
            self.hidden_layer(embeddings)
        )


        logits = self.output_layer(
            hidden_output
        )


        loss = None


        if targets is not None:

            batch, time, channels = logits.shape


            logits_for_loss = logits.view(
                batch * time,
                channels,
            )


            targets_for_loss = targets.view(
                batch * time
            )


            loss = F.cross_entropy(
                logits_for_loss,
                targets_for_loss,
            )


        return logits, loss


    def generate(
        self,
        input_ids,
        max_new_tokens,
    ):

        for _ in range(max_new_tokens):

            latest_input = input_ids[:, -block_size:]


            logits, _ = self(
                latest_input
            )


            last_token_logits = logits[:, -1, :]


            probabilities = F.softmax(
                last_token_logits,
                dim=-1,
            )


            next_token = torch.multinomial(
                probabilities,
                num_samples=1,
            )


            input_ids = torch.cat(
                [input_ids, next_token],
                dim=1,
            )


        return input_ids



# ============================================================
# 8. CREATE MODEL
# ============================================================

model = TinyLanguageModel()


print("\nModel:")

print(model)


# ============================================================
# 9. CREATE OPTIMIZER
# ============================================================

optimizer = torch.optim.AdamW(
    model.parameters(),
    lr=learning_rate,
)

# ============================================================
# 10. TRAIN THE MODEL
# ============================================================

print("\nTraining Started...\n")

for step in range(training_steps):

    inputs, targets = get_batch()


    logits, loss = model(
        inputs,
        targets,
    )


    optimizer.zero_grad()


    loss.backward()


    optimizer.step()


    if step % 300 == 0:

        print(
            "Step:",
            step,
            "Loss:",
            round(loss.item(), 4),
        )


print("\nTraining Completed.")

# ============================================================
# 11. GENERATE TEXT
# ============================================================

start_text = input("Enter text : ")

start_tokens = torch.tensor(
    [encode(start_text)],
    dtype=torch.long,
)

generated_tokens = model.generate(
    start_tokens,
    max_new_tokens=100,
)

generated_text = decode(
    generated_tokens[0].tolist()
)

print("\nGenerated Text:\n")

print(generated_text)

