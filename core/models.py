from django.db import models


class Instituto(models.Model):
    nome = models.TextField(max_length=50, null=False, verbose_name='nome')
    ativo = models.BooleanField(default=True, verbose_name='ativo')
    data_cadastro = models.DateField(auto_now_add=True,
                                     verbose_name='cadastrado em')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Instituto'
        verbose_name_plural = 'Institutos'


class ItemRsc(models.Model):
    instituto = models.ManyToManyField(Instituto, related_name='Instituto')
    niveis_rsc = [('RSCI', '1'), ('RSCII', '2'), ('RSCIII', '3')]
    nivel = models.CharField(choices=niveis_rsc, max_length=6)
    numeracao = models.CharField(max_length=2, blank=False, null=False)
    peso = models.IntegerField(max_length=2, default=1)
    valor_maximo = models.IntegerField(max_length=2, blank=False, null=False)
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.instituto} - {self.numeracao}'

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'


class SubItem(models.Model):
    item = models.ForeignKey(ItemRsc, related_name='item',
                             on_delete=models.CASCADE)
    numeracao = models.CharField(max_length=2, blank=False, null=False)
    valor = models.DecimalField(max_digits=4, decimal_places=2, blank=False,
                                null=False)
    valor_maximo = models.IntegerField(max_length=2, blank=False, null=False)
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.item} - {self.numeracao}'

    class Meta:
        verbose_name = 'Subitem'
        verbose_name_plural = 'Subitens'
