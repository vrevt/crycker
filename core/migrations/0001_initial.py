# Generated by Django 3.2.8 on 2021-11-02 20:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalOrder',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('ticker', models.CharField(max_length=20)),
                ('buy_price', models.DecimalField(decimal_places=18, max_digits=100)),
                ('amount', models.DecimalField(decimal_places=18, max_digits=100)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical order',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market_name', models.CharField(max_length=20)),
                ('start_cash', models.DecimalField(decimal_places=2, max_digits=10)),
                ('now_cash', models.DecimalField(decimal_places=2, max_digits=10)),
                ('free_cash', models.DecimalField(decimal_places=2, max_digits=10)),
                ('all_profit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fixed_profit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=20)),
                ('buy_price', models.DecimalField(decimal_places=18, max_digits=100)),
                ('amount', models.DecimalField(decimal_places=18, max_digits=100)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('market', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='market', to='core.market')),
            ],
        ),
    ]
