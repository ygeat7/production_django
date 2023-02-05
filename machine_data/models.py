from django.db import models

class MachineData(models.Model):
    new_l_processsettingname = models.TextField(db_column='new_l_processsettingName', primary_key=True)  # Field name made lowercase.
    new_l_customername = models.TextField(db_column='new_l_customerName', blank=True, null=True)  # Field name made lowercase.
    new_l_headspecificationname = models.TextField(db_column='new_l_headspecificationName', blank=True, null=True)  # Field name made lowercase.
    new_l_machinehistoryname = models.TextField(db_column='new_l_machinehistoryName', blank=True, null=True)  # Field name made lowercase.
    new_p_machinemanufacturer = models.TextField(blank=True, null=True)
    new_p_framemanufacturer = models.TextField(blank=True, null=True)
    new_p_covermanufacturer = models.TextField(blank=True, null=True)
    new_dt_materials = models.DateTimeField(blank=True, null=True)
    new_dt_endelectronics = models.DateTimeField(blank=True, null=True)
    new_dt_coverin = models.DateTimeField(blank=True, null=True)
    new_dt_machinesettingstart = models.DateTimeField(blank=True, null=True)
    new_dt_machinesettingend = models.DateTimeField(blank=True, null=True)
    new_dt_inspectiondate = models.DateTimeField(blank=True, null=True)
    new_ntxt_optiondetails = models.TextField(blank=True, null=True)
    new_ntxt_etcdetails = models.TextField(blank=True, null=True)
    location = models.TextField(db_column='Location', blank=True, null=True)  # Field name made lowercase.
    new_workeryominame = models.TextField(db_column='new_workerYomiName', blank=True, null=True)  # Field name made lowercase.
    new_modelgroupname = models.TextField(db_column='new_modelgroupName', blank=True, null=True)  # Field name made lowercase.
    new_dt_request = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'machine_data'

    def __str__(self):
        return f'[{self.new_l_processsettingname}({self.new_l_machinehistoryname})]{self.new_modelgroupname}'

    def get_absolute_url(self):
        return f'/machinedata/{self.pk}'