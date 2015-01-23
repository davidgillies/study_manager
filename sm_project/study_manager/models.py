from django.db import models
from eventlog.models import log
from django.contrib.auth.models import User


class Surgery(models.Model):
    name = models.CharField(max_length=50, blank=True)
    addr1 = models.CharField(max_length=50, blank=True)
    addr2 = models.CharField(max_length=50, blank=True)
    town = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    post_code = models.CharField(max_length=50, blank=True)
    telephone = models.CharField(max_length=12, blank=True)
    admin_contact_name = models.CharField(max_length=50, blank=True)
    admin_contact_title = models.CharField(max_length=50, blank=True)
    notes = models.TextField(blank=True)
    funding_notes = models.TextField(blank=True)
    full_name = models.CharField(max_length=70, blank=True)
    surgery_lab_id = models.CharField(max_length=50, blank=True)
    surgery_barcode = models.CharField(max_length=25, blank=True)
    study_survey = models.NullBooleanField()
    created = models.DateField()
    created_by = models.CharField(max_length=50, blank=True)
    modified = models.DateField(null=True, blank=True)
    modified_by = models.CharField(max_length=50, blank=True)
    gp_practice_code = models.CharField(max_length=6, blank=True)
    recruitment_surgery = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id:
            log(user=self.user, action='added', extra={'Name':self.name})
        else:
            log(user=self.user, action='updated', extra={'Name':self.name})
        super(Surgery, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class GP(models.Model):
    surgery_id = models.ForeignKey(Surgery)
    gp_name = models.CharField(max_length=50, blank=True)
    created = models.DateField()
    created_by = models.CharField(max_length=50)
    modified = models.DateField(null=True, blank=True)
    modified_by = models.CharField(max_length=50, blank=True)
    gp_code = models.CharField(max_length=8, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.id:
            log(user=self.user, action='added',  extra={'Name':self.gp_name})
        else:
            log(user=self.user, action='updated', extra={'Name':self.gp_name})
        super(GP, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return self.gp_name

    def __str__(self):
        return self.gp_name


class Volunteer(models.Model):
    volunteer_id = models.CharField(max_length=8, blank=True)
    part_id = models.IntegerField(null=True, blank=False)
    barcode = models.CharField(max_length=50, blank=True)
    nhs_id = models.CharField(max_length=10, blank=True)
    title = models.CharField(max_length=10, blank=True)
    initials = models.CharField(max_length=10, blank=True)
    fore_names = models.CharField(max_length=50, blank=True)
    surname = models.CharField(max_length=50, blank=True)
    dob = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=1, blank=True) # CHOICES
    addr1 = models.CharField(max_length=50, blank=True)
    addr2 = models.CharField(max_length=50, blank=True)
    town = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    post_code = models.CharField(max_length=50, blank=True)
    home_tel = models.CharField(max_length=50, blank=True)
    work_tel = models.CharField(max_length=50, blank=True)
    mob_tel = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    surgery_id = models.ForeignKey(Surgery)
    gp_id = models.ForeignKey(GP)
    status = models.IntegerField(null=True, blank=True) # CHOICES
    date = models.DateField(null=True, blank=True)
    reason = models.IntegerField(null=True, blank=True) # CHOICES?
    comment = models.TextField(blank=True)
    test_site = models.CharField(max_length=15, blank=True)
    user_name = models.CharField(max_length=50, blank=True)
    edit_mode = models.BooleanField(default=False)
    editor = models.CharField(max_length=50, blank=True)
    modified =  models.DateField(null=True, blank=True)
    modified_by = models.CharField(max_length=50, blank=True)
    created =  models.DateField(null=True, blank=True)
    created_by = models.CharField(max_length=50, blank=True)
    moved_away = models.NullBooleanField(blank=True)
    diabetes_diagnosed = models.NullBooleanField()
    user=models.ForeignKey(User)
    
    def save(self, *args, **kwargs):
        if not self.id:
            log(user=self.user, action='added',  extra={'Name':self.surname})
        else:
            log(user=self.user, action='updated', extra={'Name':self.surname})
        super(Volunteer, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return '%s %s' % (self.fore_names, self.surname)

    def __str__(self):
        return '%s %s' % (self.fore_names, self.surname)


class Appointment(models.Model):
    volunteer_id = models.ForeignKey(Volunteer)
    site_informed = models.BooleanField(default=False)
    repeat = models.BooleanField(default=False)
    site = models.CharField(max_length=10, blank=True)
    app_date =  models.DateField(null=True, blank=True)
    app_time = models.TimeField(null=True, blank=True)
    monitor_allocated = models.IntegerField(null=True, blank=True)
    created =  models.DateField()
    created_by = models.CharField(max_length=50, blank=True)
    modified =  models.DateField(null=True, blank=True)
    modified_by = models.CharField(max_length=50, blank=True)
    study_phase = models.IntegerField(null=True, blank=True) # CHOICES
    app_status = models.IntegerField(null=True, blank=True) # Choices
    
    def save(self, *args, **kwargs):
        if not self.id:
            log(user=self.user, action='added',  extra={'Date':self.app_date, 'Time': self.app_time})
        else:
            log(user=self.user, action='updated', extra={'Date':self.app_date, 'Time': self.app_time})
        super(Appointment, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return '%s %s' % (self.volunteer_id.fore_names, self.voluntee_id.surname)

    def __str__(self):
        return '%s %s' % (self.volunteer_id.fore_names, self.volunteer_id.surname)
