from django.db import models


class PKMOrder(models.Model):
    number = models.CharField(unique=True, max_length=100)
    date_receipt = models.DateField()
    required_completion_date = models.DateField()
    priority = models.IntegerField(blank=True, null=True)
    order_status = models.ForeignKey('PKMOrderstatus', models.DO_NOTHING, blank=True, null=True)
    calculated_completion_date = models.DateField(blank=True, null=True)
    actual_completion_date = models.DateField(blank=True, null=True)
    customer = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PKMOrder'


class PKMUser(models.Model):
    login = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    role = models.ForeignKey('PKMRole', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PKMUser'


class PKMAllocation(models.Model):
    role = models.ForeignKey('PKMRole', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(PKMUser, models.DO_NOTHING, blank=True, null=True)
    area = models.ForeignKey('PKMArea', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PKMAllocation'


class PKMArea(models.Model):
    name = models.CharField(max_length=255)
    indent = models.IntegerField(blank=True, null=True)
    department = models.ForeignKey('PKMDepartment', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PKMArea'

class PKMBatch(models.Model):
    name = models.CharField(max_length=255)
    count = models.IntegerField(blank=True, null=True)
    code = models.CharField(unique=True, max_length=100, blank=True, null=True)
    technology = models.TextField(blank=True, null=True)
    isready = models.BooleanField(blank=True, null=True)
    order = models.ForeignKey(PKMOrder, models.DO_NOTHING, blank=True, null=True)
    bath_archive = models.ForeignKey('PKMBatcharchive', models.DO_NOTHING, blank=True, null=True)
    batch_status = models.ForeignKey('PKMBatchstatus', models.DO_NOTHING, blank=True, null=True)
    rs_number = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PKMBatch'


class PKMBatcharchive(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(unique=True, max_length=100)
    technology_number = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PKMBatcharchive'


class PKMBatchstatus(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'PKMBatchstatus'


class PKMChiefbatch(models.Model):
    bath = models.ForeignKey(PKMBatch, models.DO_NOTHING, blank=True, null=True)
    batch_status = models.ForeignKey(PKMBatchstatus, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PKMChiefbatch'


class PKMChiefdistribution(models.Model):
    stage = models.ForeignKey('PKMStage', models.DO_NOTHING, blank=True, null=True)
    operation = models.ForeignKey('PKMOperation', models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    batch = models.ForeignKey(PKMBatch, models.DO_NOTHING, blank=True, null=True)
    unit = models.ForeignKey('PKMDepartment', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PKMChiefdistribution'


class PKMChiefoperation(models.Model):
    chief_batch = models.ForeignKey(PKMChiefbatch, models.DO_NOTHING, blank=True, null=True)
    stage = models.ForeignKey('PKMStage', models.DO_NOTHING, blank=True, null=True)
    operation = models.ForeignKey('PKMOperation', models.DO_NOTHING, blank=True, null=True)
    is_distributed = models.BooleanField(blank=True, null=True)
    distribution_stage = models.ForeignKey('PKMStagedistribution', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PKMChiefoperation'


class PKMCompany(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=100)
    is_paid = models.BooleanField(blank=True, null=True)
    paid_machines_quantity = models.IntegerField(blank=True, null=True)
    date_of_start = models.DateField()
    date_of_end = models.DateField(blank=True, null=True)
    is_testdrive = models.BooleanField(blank=True, null=True)
    number_of_support_staff = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PKMCompany'


class PKMDepartment(models.Model):
    name = models.CharField(max_length=255)
    field = models.ForeignKey('PKMField', models.DO_NOTHING, blank=True, null=True)
    indent = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    areas_quantity = models.IntegerField(blank=True, null=True)
    machines_quantity = models.IntegerField(blank=True, null=True)
    operators_quantity = models.IntegerField(blank=True, null=True)
    support_stuff_quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PKMDepartment'


class PKMDetailmachinetype(models.Model):
    name = models.CharField(max_length=255)
    first_machine_type = models.ForeignKey('PKMFirstmachinetype', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PKMDetailmachinetype'


class PKMField(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'PKMField'


class PKMFirstmachinetype(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'PKMFirstmachinetype'


class PKMMachine(models.Model):
    invent_number = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=255)
    area = models.ForeignKey(PKMArea, models.DO_NOTHING, blank=True, null=True)
    is_activated = models.BooleanField(blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    shift_schedule = models.ForeignKey('PKMShiftschedule', models.DO_NOTHING, blank=True, null=True)
    prefix = models.CharField(max_length=50, blank=True, null=True)
    first_machine_type = models.ForeignKey(PKMFirstmachinetype, models.DO_NOTHING, blank=True, null=True)
    second_machine_type = models.ForeignKey('PKMSecondmachinetype', models.DO_NOTHING, blank=True, null=True)
    detail_machine_type = models.ForeignKey(PKMDetailmachinetype, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PKMMachine'


class PKMMachinework(models.Model):
    start_time = models.DateTimeField()
    stop_time = models.DateTimeField(blank=True, null=True)
    work_status = models.ForeignKey('PKMWorkstatus', models.DO_NOTHING, blank=True, null=True)
    machine = models.ForeignKey(PKMMachine, models.DO_NOTHING, blank=True, null=True)
    batch = models.ForeignKey(PKMBatch, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    shift = models.ForeignKey('PKMShift', models.DO_NOTHING, blank=True, null=True)
    date = models.DateField()
    indent = models.IntegerField(blank=True, null=True)
    time_working = models.DurationField(blank=True, null=True)
    isactive = models.BooleanField(blank=True, null=True)
    first_start_batch = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(PKMUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PKMMachinework'


class PKMOperation(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, blank=True, null=True)
    time_pz = models.DurationField(blank=True, null=True)
    time_sh = models.DurationField(blank=True, null=True)
    stage = models.ForeignKey('PKMStage', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PKMOperation'


class PKMOperationarchive(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, blank=True, null=True)
    time_pz = models.DurationField(blank=True, null=True)
    time_sh = models.DurationField(blank=True, null=True)
    stage_archive = models.ForeignKey('PKMStagearchive', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PKMOperationarchive'


class PKMOperationoperator(models.Model):
    time_plan = models.DurationField(blank=True, null=True)
    time_first_start = models.DateTimeField(blank=True, null=True)
    time_start = models.DateTimeField(blank=True, null=True)
    time_stop = models.DateTimeField(blank=True, null=True)
    time_working = models.DurationField(blank=True, null=True)
    stage_status = models.ForeignKey('PKMStagestatus', models.DO_NOTHING, blank=True, null=True)
    batch = models.ForeignKey(PKMBatch, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(PKMOrder, models.DO_NOTHING, blank=True, null=True)
    machine = models.ForeignKey(PKMMachine, models.DO_NOTHING, blank=True, null=True)
    operation = models.ForeignKey(PKMOperation, models.DO_NOTHING, blank=True, null=True)
    area = models.ForeignKey(PKMArea, models.DO_NOTHING, blank=True, null=True)
    chief_operation = models.ForeignKey(PKMChiefoperation, models.DO_NOTHING, blank=True, null=True)
    chief_batch = models.ForeignKey(PKMChiefbatch, models.DO_NOTHING, blank=True, null=True)
    pause = models.BooleanField(blank=True, null=True)
    optimal_part = models.CharField(max_length=255, blank=True, null=True)
    modific = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    distribution_stage = models.ForeignKey('PKMStagedistribution', models.DO_NOTHING, blank=True, null=True)
    staff = models.ForeignKey(PKMUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PKMOperationoperator'


class PKMOrderstatus(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'PKMOrderstatus'


class PKMReporttype(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'PKMReporttype'


class PKMRole(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'PKMRole'


class PKMSecondmachinetype(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'PKMSecondmachinetype'


class PKMShift(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PKMShift'


class PKMShiftdistribution(models.Model):
    date = models.DateField()
    change = models.ForeignKey(PKMShift, models.DO_NOTHING, blank=True, null=True)
    machine = models.ForeignKey(PKMMachine, models.DO_NOTHING, blank=True, null=True)
    staff = models.ForeignKey(PKMUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PKMShiftdistribution'


class PKMShiftschedule(models.Model):
    time_change = models.TimeField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    time_first = models.TimeField(blank=True, null=True)
    days = models.IntegerField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PKMShiftschedule'


class PKMStage(models.Model):
    name = models.CharField(max_length=255)
    isdistributed = models.BooleanField(blank=True, null=True)
    area = models.ForeignKey(PKMArea, models.DO_NOTHING, blank=True, null=True)
    batch = models.ForeignKey(PKMBatch, models.DO_NOTHING, blank=True, null=True)
    batch_archive = models.ForeignKey(PKMBatcharchive, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PKMStage'


class PKMStagearchive(models.Model):
    name = models.CharField(max_length=255)
    batch_archive = models.ForeignKey(PKMBatcharchive, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PKMStagearchive'


class PKMStagedistribution(models.Model):
    stage = models.ForeignKey(PKMStage, models.DO_NOTHING, blank=True, null=True)
    chief_batch = models.ForeignKey(PKMChiefbatch, models.DO_NOTHING, blank=True, null=True)
    stage_status = models.ForeignKey('PKMStagestatus', models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(PKMDepartment, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PKMStagedistribution'


class PKMStagestatus(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'PKMStagestatus'


class PKMTransfer(models.Model):
    number = models.IntegerField()
    time_sh = models.DurationField(blank=True, null=True)
    operation = models.ForeignKey(PKMOperation, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PKMTransfer'


class PKMTransferarchive(models.Model):
    time_sh = models.DurationField(blank=True, null=True)
    operation_archive = models.ForeignKey(PKMOperationarchive, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PKMTransferarchive'


class PKMTransferoperation(models.Model):
    time_first_start = models.DateTimeField(blank=True, null=True)
    time_start = models.DateTimeField(blank=True, null=True)
    time_stop = models.DateTimeField(blank=True, null=True)
    time_working = models.DurationField(blank=True, null=True)
    batch = models.ForeignKey(PKMBatch, models.DO_NOTHING, blank=True, null=True)
    machine = models.ForeignKey(PKMMachine, models.DO_NOTHING, blank=True, null=True)
    operation = models.ForeignKey(PKMOperation, models.DO_NOTHING, blank=True, null=True)
    chief_operation = models.ForeignKey(PKMChiefoperation, models.DO_NOTHING, blank=True, null=True)
    pause = models.BooleanField(blank=True, null=True)
    staff = models.ForeignKey(PKMUser, models.DO_NOTHING, blank=True, null=True)
    opt_path = models.TextField(blank=True, null=True)
    transfer = models.ForeignKey(PKMTransfer, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(PKMOrder, models.DO_NOTHING, blank=True, null=True)
    operator_operation = models.ForeignKey(PKMOperationoperator, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PKMTransferoperation'


class PKMUploadedreport(models.Model):
    number = models.CharField(max_length=100)
    staff = models.ForeignKey(PKMUser, models.DO_NOTHING, blank=True, null=True)
    report_type = models.ForeignKey(PKMReporttype, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PKMUploadedreport'


class PKMVersion(models.Model):
    version = models.CharField(max_length=50)
    link_update = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PKMVersion'


class PKMWorkershift(models.Model):
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    isactive = models.BooleanField(blank=True, null=True)
    change = models.ForeignKey(PKMShift, models.DO_NOTHING, blank=True, null=True)
    date = models.DateField()
    staff = models.ForeignKey(PKMUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PKMWorkershift'


class PKMWorkstatus(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'PKMWorkstatus'
