from django.db import models

class Vitin (models.Model):
    id = models.AutoField(primary_key=True)
    tutor_cod = models.CharField( max_length=30,verbose_name='Código do tutor', db_column='tutor_cod')
    data_interdicao = models.DateField(verbose_name='Data da interdição', db_column='data_interdicao')
    data_mandado = models.DateField(verbose_name='Data do mandado', db_column='data_mandado')
    data_sentenca = models.DateField(verbose_name='Data da sentença', db_column='data _sentenca')
    data_nascimento_interdicao = models.DateField(verbose_name='Data de nascimento', db_column='data_nascimento_interdicao')
    num_processo = models.CharField(max_length=60, verbose_name='Processo', db_column='num_processo')
    nome_juiz_mandado = models.CharField(max_length=200, verbose_name='Nome do mandado', db_column='nome_juiz_mandado')
    nome_juiz_sentenca = models.CharField(max_length=200, verbose_name='Nome da sentença', db_column='nome_juiz_sentenca')
    nome_interditado = models.CharField(max_length=100, verbose_name='Nome', db_column='nome_interditado')
    nacionalidade_interditado = models.CharField(max_length=50, verbose_name='Nacionalidade', db_column='nacionalidade_interditado')
    nome_pai_interditado = models.CharField(max_length=100, verbose_name='Nome do pai', db_column='nome_pai_interditado')
    nome_mae_interditado = models.CharField(max_length=100, verbose_name='Nome da mãe', db_column='nome_mae_interditado')
    endereco_interditado = models.CharField(max_length=100, verbose_name='Endereço', db_column='endereco_interditado')
    bairro_interditado = models.CharField(max_length=40, verbose_name='Bairro', db_column='bairro_interditado')
    cidade_interditado = models.CharField(max_length=30, verbose_name='Cidade', db_column='cidade_interditado')
    cartorio_certidao_nascimento = models.CharField(max_length=150, verbose_name='Certidão de nascimento', db_column='cartorio_certidao_nascimento')
    livro_certidao_nascimento = models.CharField(max_length=30, verbose_name='Livro de certidão de nascimento', db_column='livro_certidao_nascimento')
    folha_certidao_nascimento = models.CharField(max_length=30, verbose_name='Folha da certidão de nascimento', db_column='folha_certidao_nascimento')
    termo_certidao_nascimento = models.CharField(max_length=30, verbose_name='Termo da certidão de nascimento', db_column='termo_certidao_nascimento')
    livro = models.CharField(max_length=20, verbose_name='Livro', db_column='livro')
    folha = models.CharField(max_length=20, verbose_name='Folha', db_column='folha')
    termo = models.CharField(max_length=20, verbose_name='Termo', db_column='termo')
    observation = models.TextField(max_length=80, verbose_name='Observação', db_column='observation')
    matricula = models.CharField(max_length=50, verbose_name='Matrícula', db_column='matricula')
    cpfinterditado = models.CharField(max_length=50, verbose_name='CPF', db_column='cpfinterditado')


class Meta:
        """Defining the class name within the database"""

        db_table = "vitins"