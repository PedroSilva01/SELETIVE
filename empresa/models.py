from django.db import models

# Create your models here.
# here is where a connectionwith db happens.
#sempre que quizer criar uma tabela a classe precisa herdar de models.Model
#e para criar uma coluna usa-se: nomaDaTabela = models.TipoDeDado


class Tecnologia(models.Model):
    tecnologia = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.tecnologia


class Empresa(models.Model):
    choices_nicho_mercado = (
        ('M', 'Marketing'),
        ('N', 'Nutrição'),
        ('D', 'Design'),
        ('T', 'Tecnologia')
    )
    logo = models.ImageField(upload_to="logo_empresa", null=True)
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    cidade = models.CharField(max_length=50)
    endereco = models.CharField(max_length=30)
    caracteristicas_empresa = models.TextField()
    tecnologias = models.ManyToManyField(Tecnologia)
    nicho_mercado = models.CharField(max_length=3, choices=choices_nicho_mercado)

    def __str__(self):
        return self.nome


class Vagas(models.Model):
    choices_experiencia = (
        ('J', 'Júnior'),
        ('P', 'Pleno'),
        ('S', 'Sênior')
    )

    choices_status = (
        ('I', 'Interesse'),
        ('C', 'Currículo enviado'),
        ('E', 'Entrevista'),
        ('D', 'Desafio técnico'),
        ('F', 'Finalizado')
    )
    #A FOREIGNKEY É USADA QUANDO A EMPRESA PODE TER MUITAS VAGAS, MAS 1 VAGA SÓ PODE SER DE 1 EMPRESA.
    empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=30)
    nivel_experiencia = models.CharField(max_length=2, choices=choices_experiencia)
    data_final = models.DateField()
    status = models.CharField(max_length=30, choices=choices_status)
    tecnologias_dominadas = models.ManyToManyField(Tecnologia)
    tecnologias_estudar = models.ManyToManyField(Tecnologia, related_name='estudar')


    def __str__(self):
        return self.titulo