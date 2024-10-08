from django.db import models


class NTZOrder(models.Model):
    number = models.CharField(unique=True, max_length=100)
    date_receipt = models.DateField()
    required_completion_date = models.DateField()
    priority = models.IntegerField(blank=True, null=True)
    order_status = models.ForeignKey('NTZOrderstatus', models.DO_NOTHING, blank=True, null=True)
    calculated_completion_date = models.DateField(blank=True, null=True)
    actual_completion_date = models.DateField(blank=True, null=True)
    customer = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NTZOrder'


class NTZUser(models.Model):
    login = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    role = models.ForeignKey('NTZRole', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NTZUser'


class NTZAllocation(models.Model):
    role = models.ForeignKey('NTZRole', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(NTZUser, models.DO_NOTHING, blank=True, null=True)
    area = models.ForeignKey('NTZArea', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NTZAllocation'


class NTZArea(models.Model):
    name = models.CharField(max_length=255)
    indent = models.IntegerField(blank=True, null=True)
    department = models.ForeignKey('NTZDepartment', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NTZArea'

class NTZBatch(models.Model):
    name = models.CharField(max_length=255)
    count = models.IntegerField(blank=True, null=True)
    code = models.CharField(unique=True, max_length=100, blank=True, null=True)
    technology = models.TextField(blank=True, null=True)
    isready = models.BooleanField(blank=True, null=True)
    order = models.ForeignKey(NTZOrder, models.DO_NOTHING, blank=True, null=True)
    bath_archive = models.ForeignKey('NTZBatcharchive', models.DO_NOTHING, blank=True, null=True)
    batch_status = models.ForeignKey('NTZBatchstatus', models.DO_NOTHING, blank=True, null=True)
    rs_number = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NTZBatch'


class NTZBatcharchive(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(unique=True, max_length=100)
    technology_number = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NTZBatcharchive'


class NTZBatchstatus(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'NTZBatchstatus'


class NTZChiefbatch(models.Model):
    bath = models.ForeignKey(NTZBatch, models.DO_NOTHING, blank=True, null=True)
    batch_status = models.ForeignKey(NTZBatchstatus, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NTZChiefbatch'


class NTZChiefdistribution(models.Model):
    stage = models.ForeignKey('NTZStage', models.DO_NOTHING, blank=True, null=True)
    operation = models.ForeignKey('NTZOperation', models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    batch = models.ForeignKey(NTZBatch, models.DO_NOTHING, blank=True, null=True)
    unit = models.ForeignKey('NTZDepartment', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NTZChiefdistribution'


class NTZChiefoperation(models.Model):
    chief_batch = models.ForeignKey(NTZChiefbatch, models.DO_NOTHING, blank=True, null=True)
    stage = models.ForeignKey('NTZStage', models.DO_NOTHING, blank=True, null=True)
    operation = models.ForeignKey('NTZOperation', models.DO_NOTHING, blank=True, null=True)
    is_distributed = models.BooleanField(blank=True, null=True)
    distribution_stage = models.ForeignKey('NTZStagedistribution', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NTZChiefoperation'


class NTZCompany(models.Model):
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
        db_table = 'NTZCompany'


class NTZDepartment(models.Model):
    name = models.CharField(max_length=255)
    field = models.ForeignKey('NTZField', models.DO_NOTHING, blank=True, null=True)
    indent = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    areas_quantity = models.IntegerField(blank=True, null=True)
    machines_quantity = models.IntegerField(blank=True, null=True)
    operators_quantity = models.IntegerField(blank=True, null=True)
    support_stuff_quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NTZDepartment'


class NTZDetailmachinetype(models.Model):
    name = models.CharField(max_length=255)
    first_machine_type = models.ForeignKey('NTZFirstmachinetype', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NTZDetailmachinetype'


class NTZField(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'NTZField'


class NTZFirstmachinetype(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'NTZFirstmachinetype'


class NTZMachine(models.Model):
    invent_number = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=255)
    area = models.ForeignKey(NTZArea, models.DO_NOTHING, blank=True, null=True)
    is_activated = models.BooleanField(blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    shift_schedule = models.ForeignKey('NTZShiftschedule', models.DO_NOTHING, blank=True, null=True)
    prefix = models.CharField(max_length=50, blank=True, null=True)
    first_machine_type = models.ForeignKey(NTZFirstmachinetype, models.DO_NOTHING, blank=True, null=True)
    second_machine_type = models.ForeignKey('NTZSecondmachinetype', models.DO_NOTHING, blank=True, null=True)
    detail_machine_type = models.ForeignKey(NTZDetailmachinetype, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NTZMachine'


class NTZMachinework(models.Model):
    start_time = models.DateTimeField()
    stop_time = models.DateTimeField(blank=True, null=True)
    work_status = models.ForeignKey('NTZWorkstatus', models.DO_NOTHING, blank=True, null=True)
    machine = models.ForeignKey(NTZMachine, models.DO_NOTHING, blank=True, null=True)
    batch = models.ForeignKey(NTZBatch, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    shift = models.ForeignKey('NTZShift', models.DO_NOTHING, blank=True, null=True)
    date = models.DateField()
    indent = models.IntegerField(blank=True, null=True)
    time_working = models.DurationField(blank=True, null=True)
    isactive = models.BooleanField(blank=True, null=True)
    first_start_batch = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(NTZUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NTZMachinework'


class NTZOperation(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, blank=True, null=True)
    time_pz = models.DurationField(blank=True, null=True)
    time_sh = models.DurationField(blank=True, null=True)
    stage = models.ForeignKey('NTZStage', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NTZOperation'


class NTZOperationarchive(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, blank=True, null=True)
    time_pz = models.DurationField(blank=True, null=True)
    time_sh = models.DurationField(blank=True, null=True)
    stage_archive = models.ForeignKey('NTZStagearchive', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NTZOperationarchive'


class NTZOperationoperator(models.Model):
    time_plan = models.DurationField(blank=True, null=True)
    time_first_start = models.DateTimeField(blank=True, null=True)
    time_start = models.DateTimeField(blank=True, null=True)
    time_stop = models.DateTimeField(blank=True, null=True)
    time_working = models.DurationField(blank=True, null=True)
    stage_status = models.ForeignKey('NTZStagestatus', models.DO_NOTHING, blank=True, null=True)
    batch = models.ForeignKey(NTZBatch, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(NTZOrder, models.DO_NOTHING, blank=True, null=True)
    machine = models.ForeignKey(NTZMachine, models.DO_NOTHING, blank=True, null=True)
    operation = models.ForeignKey(NTZOperation, models.DO_NOTHING, blank=True, null=True)
    area = models.ForeignKey(NTZArea, models.DO_NOTHING, blank=True, null=True)
    chief_operation = models.ForeignKey(NTZChiefoperation, models.DO_NOTHING, blank=True, null=True)
    chief_batch = models.ForeignKey(NTZChiefbatch, models.DO_NOTHING, blank=True, null=True)
    pause = models.BooleanField(blank=True, null=True)
    optimal_part = models.CharField(max_length=255, blank=True, null=True)
    modific = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    distribution_stage = models.ForeignKey('NTZStagedistribution', models.DO_NOTHING, blank=True, null=True)
    staff = models.ForeignKey(NTZUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NTZOperationoperator'


class NTZOrderstatus(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'NTZOrderstatus'


class NTZReporttype(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'NTZReporttype'


class NTZRole(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'NTZRole'


class NTZSecondmachinetype(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'NTZSecondmachinetype'


class NTZShift(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NTZShift'


class NTZShiftdistribution(models.Model):
    date = models.DateField()
    change = models.ForeignKey(NTZShift, models.DO_NOTHING, blank=True, null=True)
    machine = models.ForeignKey(NTZMachine, models.DO_NOTHING, blank=True, null=True)
    staff = models.ForeignKey(NTZUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NTZShiftdistribution'


class NTZShiftschedule(models.Model):
    time_change = models.TimeField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    time_first = models.TimeField(blank=True, null=True)
    days = models.IntegerField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NTZShiftschedule'


class NTZStage(models.Model):
    name = models.CharField(max_length=255)
    isdistributed = models.BooleanField(blank=True, null=True)
    area = models.ForeignKey(NTZArea, models.DO_NOTHING, blank=True, null=True)
    batch = models.ForeignKey(NTZBatch, models.DO_NOTHING, blank=True, null=True)
    batch_archive = models.ForeignKey(NTZBatcharchive, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NTZStage'


class NTZStagearchive(models.Model):
    name = models.CharField(max_length=255)
    batch_archive = models.ForeignKey(NTZBatcharchive, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NTZStagearchive'


class NTZStagedistribution(models.Model):
    stage = models.ForeignKey(NTZStage, models.DO_NOTHING, blank=True, null=True)
    chief_batch = models.ForeignKey(NTZChiefbatch, models.DO_NOTHING, blank=True, null=True)
    stage_status = models.ForeignKey('NTZStagestatus', models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(NTZDepartment, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NTZStagedistribution'


class NTZStagestatus(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'NTZStagestatus'


class NTZTransfer(models.Model):
    number = models.IntegerField()
    time_sh = models.DurationField(blank=True, null=True)
    operation = models.ForeignKey(NTZOperation, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NTZTransfer'


class NTZTransferarchive(models.Model):
    time_sh = models.DurationField(blank=True, null=True)
    operation_archive = models.ForeignKey(NTZOperationarchive, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NTZTransferarchive'


class NTZTransferoperation(models.Model):
    time_first_start = models.DateTimeField(blank=True, null=True)
    time_start = models.DateTimeField(blank=True, null=True)
    time_stop = models.DateTimeField(blank=True, null=True)
    time_working = models.DurationField(blank=True, null=True)
    batch = models.ForeignKey(NTZBatch, models.DO_NOTHING, blank=True, null=True)
    machine = models.ForeignKey(NTZMachine, models.DO_NOTHING, blank=True, null=True)
    operation = models.ForeignKey(NTZOperation, models.DO_NOTHING, blank=True, null=True)
    chief_operation = models.ForeignKey(NTZChiefoperation, models.DO_NOTHING, blank=True, null=True)
    pause = models.BooleanField(blank=True, null=True)
    staff = models.ForeignKey(NTZUser, models.DO_NOTHING, blank=True, null=True)
    opt_path = models.TextField(blank=True, null=True)
    transfer = models.ForeignKey(NTZTransfer, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(NTZOrder, models.DO_NOTHING, blank=True, null=True)
    operator_operation = models.ForeignKey(NTZOperationoperator, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NTZTransferoperation'


class NTZUploadedreport(models.Model):
    number = models.CharField(max_length=100)
    staff = models.ForeignKey(NTZUser, models.DO_NOTHING, blank=True, null=True)
    report_type = models.ForeignKey(NTZReporttype, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NTZUploadedreport'


class NTZVersion(models.Model):
    version = models.CharField(max_length=50)
    link_update = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NTZVersion'


class NTZWorkershift(models.Model):
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    isactive = models.BooleanField(blank=True, null=True)
    change = models.ForeignKey(NTZShift, models.DO_NOTHING, blank=True, null=True)
    date = models.DateField()
    staff = models.ForeignKey(NTZUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'NTZWorkershift'


class NTZWorkstatus(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'NTZWorkstatus'
