# Generated by Django 3.0.5 on 2020-05-10 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('followup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccinefollowup',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Provider'),
        ),
        migrations.AddField(
            model_name='vaccinefollowup',
            name='author_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.ProviderType'),
        ),
        migrations.AddField(
            model_name='vaccinefollowup',
            name='contact_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.ContactMethod'),
        ),
        migrations.AddField(
            model_name='vaccinefollowup',
            name='contact_resolution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='followup.ContactResult'),
        ),
        migrations.AddField(
            model_name='vaccinefollowup',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Patient'),
        ),
        migrations.AddField(
            model_name='labfollowup',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Provider'),
        ),
        migrations.AddField(
            model_name='labfollowup',
            name='author_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.ProviderType'),
        ),
        migrations.AddField(
            model_name='labfollowup',
            name='contact_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.ContactMethod'),
        ),
        migrations.AddField(
            model_name='labfollowup',
            name='contact_resolution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='followup.ContactResult'),
        ),
        migrations.AddField(
            model_name='labfollowup',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Patient'),
        ),
        migrations.AddField(
            model_name='historicalvaccinefollowup',
            name='author',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.Provider'),
        ),
        migrations.AddField(
            model_name='historicalvaccinefollowup',
            name='author_type',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.ProviderType'),
        ),
        migrations.AddField(
            model_name='historicalvaccinefollowup',
            name='contact_method',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.ContactMethod'),
        ),
        migrations.AddField(
            model_name='historicalvaccinefollowup',
            name='contact_resolution',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='followup.ContactResult'),
        ),
    ]