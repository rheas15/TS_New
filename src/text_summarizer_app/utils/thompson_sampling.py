import numpy as np

class ThompsonSampling:
    def __init__(self, alpha_bullet=1, beta_bullet=1, alpha_paragraph=1, beta_paragraph=1):
        self.alpha_bullet = alpha_bullet
        self.beta_bullet = beta_bullet
        self.alpha_paragraph = alpha_paragraph
        self.beta_paragraph = beta_paragraph

        # Initialize lists to store historical user choices
        self.bullet_choices = []
        self.paragraph_choices = []

    def sample_format(self):
        # Check if there's historical data available
        if self.bullet_choices or self.paragraph_choices:
            bullet_sample = np.random.beta(sum(self.bullet_choices) + 1,
                                           len(self.bullet_choices) - sum(self.bullet_choices) + 1)
            paragraph_sample = np.random.beta(sum(self.paragraph_choices) + 1,
                                              len(self.paragraph_choices) - sum(self.paragraph_choices)+ 1)
        else:
            # Use initial alpha and beta values
            bullet_sample = np.random.beta(self.alpha_bullet, self.beta_bullet)
            paragraph_sample = np.random.beta(self.alpha_paragraph, self.beta_paragraph)
        
        if bullet_sample > paragraph_sample:
            return "Bullet Points"
        else:
            return "Paragraph"

    def update_format_feedback(self, format_chosen):
        if format_chosen == "Bullet Points":
            self.bullet_choices.append(1)  # Record user choice for bullet points
            self.paragraph_choices.append(0)  # Record absence of user choice for paragraphs
        else:
            self.bullet_choices.append(0)  # Record absence of user choice for bullet points
            self.paragraph_choices.append(1)  # Record user choice for paragraphs