import colorfield.fields
import django.db.models.deletion
import main.mixins
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            bases=(main.mixins.SaveSlugMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('color', colorfield.fields.ColorField(blank=True, default='', image_field='image', max_length=25, samples=[('#FFFFFF', 'white'), ('#000000', 'black'), ('#FF0000', 'red'), ('#00FF00', 'green'), ('#0000FF', 'blue'), ('#FFFF00', 'yellow')])),
                ('size', models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=3)),
                ('type', models.CharField(choices=[('shoes', 'shoes'), ('t-shirt', 't-shirt'), ('sweatshirt', 'sweatshirt'), ('pants', 'pants'), ('jacket', 'jacket'), ('sunglasses', 'sunglasses')], max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.Collection')),
            ],
            bases=(main.mixins.SaveSlugMixin, models.Model),
        ),
    ]