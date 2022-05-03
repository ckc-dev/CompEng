"""'base' app models."""

from django.db import models

REQUIREMENT_PRIORITY_DEFAULT = 'Essencial'
REQUIREMENT_TYPE_DEFAULT = 'RF'
REQUIREMENT_TYPES = [
    ('RF', 'Funcional'),
    ('RNF', 'Não-funcional'),
]


class Reference(models.Model):
    """
    Model for a reference, which is used when creating requirements.

    Args:
        Model (class): Django's base model class.
    """

    is_available = models.BooleanField(default=True)
    name = models.CharField(max_length=256)
    section = models.CharField(max_length=64)
    type = models.CharField(
        max_length=4,
        choices=REQUIREMENT_TYPES,
        default=REQUIREMENT_TYPE_DEFAULT,
    )

    def __str__(self):
        """Model's string representation."""
        return f'{self.section} | {self.name}'


class Requirement(models.Model):
    """
    Model for a requirement.

    Args:
        Model (class): Django's base model class.
    """

    LATEX_TEMPLATE = """
    \\subsection{{{type}-{id}}}
        \\paragraph{{Nome}}
            \\subparagraph{{{name}}}
        \\paragraph{{Categoria}}
            \\subparagraph{{{category}}}
        \\paragraph{{Data de criação}}
            \\subparagraph{{{date}}}
        \\paragraph{{Versão}}
            \\subparagraph{{{version}}}
        \\paragraph{{Prioridade}}
            \\subparagraph{{{priority}}}
        \\paragraph{{Descrição}}
            \\subparagraph{{{description}}}"""

    author = models.CharField(max_length=64)
    reference = models.OneToOneField(
        Reference,
        on_delete=models.CASCADE,
        related_name='requirement',
    )
    type = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        choices=REQUIREMENT_TYPES,
        default=REQUIREMENT_TYPE_DEFAULT,
    )
    section = models.CharField(max_length=64, null=True, blank=True)
    name = models.CharField(max_length=256)
    category = models.CharField(max_length=64)
    date = models.DateField(auto_now_add=True)
    version = models.IntegerField(default=1)
    priority = models.CharField(
        max_length=64,
        default=REQUIREMENT_PRIORITY_DEFAULT,
    )
    description = models.TextField(max_length=16384)

    def save(self, *args, **kwargs):
        """Save an instance of this model."""
        self.type = self.reference.type
        self.section = self.reference.section
        self.reference.is_available = False
        self.reference.save()

        super(Requirement, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """Delete an instance of this model."""
        self.reference.is_available = True
        self.reference.save()

        super(Requirement, self).delete(*args, **kwargs)

    def to_latex(self, id_):
        """Return model's LaTeX representation."""
        return self.LATEX_TEMPLATE.format(
            type=self.type,
            id=str(id_).zfill(3),
            name=self.name,
            category=self.category,
            date=self.date,
            version=self.version,
            priority=self.priority,
            description=self.description,
        )

    def __str__(self):
        """Model's string representation."""
        return f'{self.author} - {self.type} (V{self.version}) | {self.name}'
