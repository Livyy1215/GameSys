# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-09 14:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GlobeMatchRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TeamPlayerPerGroup', models.IntegerField()),
                ('PlayerPerMatch', models.IntegerField()),
                ('PlayerCountInGroupScore', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('ID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('JudgeAccount', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=20)),
                ('Name', models.CharField(max_length=20)),
                ('PhoneNum', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('MatchID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Group', models.CharField(max_length=20)),
                ('Event', models.CharField(max_length=20)),
                ('StartTime', models.CharField(max_length=20)),
                ('EndTime', models.CharField(max_length=20)),
                ('MatchStatus', models.CharField(max_length=20)),
                ('MatchType', models.CharField(max_length=10)),
                ('SubGroup', models.CharField(max_length=10)),
                ('ChiefID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameAdmin.Judge')),
            ],
        ),
        migrations.CreateModel(
            name='MatchJudge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IsChief', models.BooleanField(default=0)),
                ('ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameAdmin.Judge')),
                ('MatchID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameAdmin.Match')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('PlayerID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('ID', models.CharField(max_length=20)),
                ('Name', models.CharField(max_length=20)),
                ('Age', models.IntegerField()),
                ('Group', models.CharField(max_length=20)),
                ('CultureScore', models.IntegerField()),
                ('Event', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='PlayMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DScore', models.IntegerField()),
                ('PScore', models.IntegerField()),
                ('AllScore', models.IntegerField()),
                ('ScoreState', models.IntegerField()),
                ('MatchID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameAdmin.Match')),
                ('PlayerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameAdmin.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Score', models.IntegerField()),
                ('ScoreAccept', models.IntegerField(default=0)),
                ('ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameAdmin.Judge')),
                ('MatchID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameAdmin.Match')),
                ('PlayerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameAdmin.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('TeamName', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('TeamAccount', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=20)),
                ('File', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='TeamCoach',
            fields=[
                ('ID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
                ('PhoneNum', models.CharField(max_length=20)),
                ('Gender', models.CharField(max_length=1)),
                ('TeamName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameAdmin.Team')),
            ],
        ),
        migrations.CreateModel(
            name='TeamLeader',
            fields=[
                ('ID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
                ('PhoneNum', models.CharField(max_length=20)),
                ('TeamName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameAdmin.Team')),
            ],
        ),
        migrations.CreateModel(
            name='TeamMedic',
            fields=[
                ('ID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
                ('PhoneNum', models.CharField(max_length=20)),
                ('TeamName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameAdmin.Team')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='TeamName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameAdmin.Team'),
        ),
        migrations.AddField(
            model_name='judge',
            name='TeamName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameAdmin.Team'),
        ),
        migrations.AlterUniqueTogether(
            name='score',
            unique_together=set([('MatchID', 'ID', 'PlayerID')]),
        ),
        migrations.AlterUniqueTogether(
            name='playmatch',
            unique_together=set([('MatchID', 'PlayerID')]),
        ),
        migrations.AlterUniqueTogether(
            name='matchjudge',
            unique_together=set([('MatchID', 'ID')]),
        ),
    ]
