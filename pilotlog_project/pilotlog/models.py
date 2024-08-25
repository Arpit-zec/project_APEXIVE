import uuid
from django.db import models
from django.core.exceptions import ValidationError

# Base class to include common fields
class BaseModel(models.Model):
    user_id = models.IntegerField()
    guid = models.UUIDField(unique=True)
    platform = models.IntegerField()
    _modified = models.IntegerField()

    class Meta:
        abstract = True

# Aircraft Model
class Aircraft(BaseModel):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    category = models.IntegerField()
    aircraft_class = models.IntegerField()
    power = models.IntegerField()
    seats = models.IntegerField()
    active = models.BooleanField()
    reference = models.CharField(max_length=100)
    tailwheel = models.BooleanField()
    engyype = models.IntegerField(default=0)
    complex = models.BooleanField()
    high_perf = models.BooleanField()
    aerobatic = models.BooleanField()
    fnpt = models.IntegerField()
    kg5700 = models.BooleanField()
    rating = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100)
    cond_log = models.IntegerField()
    fav_list = models.BooleanField()
    sub_model = models.CharField(max_length=100, blank=True)
    record_modified = models.IntegerField()

    def __str__(self):
        return f"{self.make} {self.model} ({self.reference})"

# Flights Model
class Flight(BaseModel):
    aircraft_id = models.ForeignKey(Aircraft, on_delete=models.CASCADE, default=1)
    date = models.DateField(null=True)
    from_airport = models.CharField(max_length=100)
    to_airport = models.CharField(max_length=100)
    route = models.TextField(blank=True)
    time_out = models.TimeField(null=True)
    time_off = models.TimeField(null=True)
    time_on = models.TimeField(null=True)
    time_in = models.TimeField(null=True)
    on_duty = models.TimeField(null=True)
    off_duty = models.TimeField(null=True)
    total_time = models.DecimalField(max_digits=5, decimal_places=2)
    pic = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sic = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    night = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    solo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cross_country = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nvg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nvg_ops = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    day_takeoffs = models.IntegerField(blank=True, null=True)
    day_landings_full_stop = models.IntegerField(blank=True, null=True)
    night_takeoffs = models.IntegerField(blank=True, null=True)
    night_landings_full_stop = models.IntegerField(blank=True, null=True)
    all_landings = models.IntegerField(blank=True, null=True)
    actual_instrument = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    simulated_instrument = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    hobbs_start = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    hobbs_end = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    tach_start = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    tach_end = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    holds = models.IntegerField(blank=True, null=True)
    approach = models.CharField(max_length=100, blank=True)

    dual_given = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    simulated_flight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    ground_training = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    instructor_name = models.CharField(max_length=100, blank=True)
    instructor_comments = models.TextField(blank=True)
    pilot_comments = models.TextField(blank=True)
    flight_review = models.BooleanField(default=False)
    checkride = models.BooleanField(default=False)
    ipc = models.BooleanField(default=False)
    nvg_proficiency = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Flight on {self.date} from {self.from_airport} to {self.to_airport}"

class ImagePic(BaseModel):
    file_ext = models.CharField(max_length=10)
    img_code = models.UUIDField(unique=True)
    file_name = models.CharField(max_length=255)
    link_code = models.UUIDField()
    img_upload = models.BooleanField(default=False)
    img_download = models.BooleanField(default=False)
    record_modified = models.IntegerField()

    def __str__(self):
        return f"ImagePic {self.file_name} ({self.img_code})"

class LimitRules(BaseModel):
    limit_code = models.UUIDField(unique=True)
    l_from = models.DateField(null=True)
    l_to = models.DateField(null=True)
    l_type = models.IntegerField()
    l_zone = models.IntegerField()
    l_minutes = models.IntegerField()
    l_period_code = models.IntegerField()
    record_modified = models.IntegerField()

    def __str__(self):
        return f"LimitRule {self.limit_code}"

class Query(BaseModel):
    name = models.CharField(max_length=255)
    mQCode = models.CharField(max_length=255)
    quick_view = models.BooleanField(default=False)
    short_name = models.CharField(max_length=255, blank=True)
    record_modified = models.IntegerField()

    def __str__(self):
        return self.name
    
class MyQueryBuild(BaseModel):
    build1 = models.TextField()
    build2 = models.IntegerField()
    build3 = models.IntegerField()
    build4 = models.CharField(max_length=255)
    mQCode = models.UUIDField()
    mQBCode = models.UUIDField()
    record_modified = models.IntegerField()

    def __str__(self):
        return f"Build for {self.mQCode}"

class Pilot(BaseModel):
    notes = models.TextField(blank=True)
    active = models.BooleanField(default=False)
    company = models.CharField(max_length=255, blank=True)
    fav_list = models.BooleanField(default=False)
    user_api = models.CharField(max_length=255, blank=True)
    facebook = models.CharField(max_length=255, blank=True)
    linkedin = models.CharField(max_length=255, blank=True)
    pilot_ref = models.CharField(max_length=255, blank=True)
    pilot_code = models.UUIDField(unique=True)
    pilot_name = models.CharField(max_length=255)
    pilot_email = models.EmailField(blank=True)
    pilot_phone = models.CharField(max_length=50, blank=True)
    certificate = models.CharField(max_length=255, blank=True)
    phone_search = models.CharField(max_length=255, blank=True)
    pilot_search = models.CharField(max_length=255, blank=True)
    roster_alias = models.CharField(max_length=255, blank=True)
    record_modified = models.IntegerField()

    def __str__(self):
        return f"Pilot {self.pilot_name} ({self.pilot_code})"
    
class Qualification(BaseModel):
    q_code = models.UUIDField(unique=True)
    ref_extra = models.IntegerField(default=0)
    ref_model = models.CharField(max_length=255, blank=True)
    validity = models.IntegerField(default=0)
    date_valid = models.DateField(null=True, blank=True)
    q_type_code = models.IntegerField(default=0)
    date_issued = models.DateField(null=True, blank=True)
    minimum_qty = models.IntegerField(default=0)
    notify_days = models.IntegerField(default=0)
    ref_airfield = models.UUIDField(default=uuid.uuid4)
    minimum_period = models.IntegerField(default=0)
    notify_comment = models.TextField(blank=True)
    record_modified = models.IntegerField()

    def __str__(self):
        return str(self.q_code)

class SettingConfig(BaseModel):
    config_code = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    group = models.CharField(max_length=255)
    data = models.TextField(blank=True)
    record_modified = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.config_code})"

class Airfield(BaseModel):
    af_code = models.CharField(max_length=255, unique=True)
    af_iata = models.CharField(max_length=10, blank=True)
    af_icao = models.CharField(max_length=10, blank=True)
    af_name = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    af_cat = models.IntegerField()
    tz_code = models.IntegerField()
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    show_list = models.BooleanField(default=False)
    user_edit = models.BooleanField(default=False)
    af_country = models.IntegerField()
    notes = models.TextField(blank=True)
    notes_user = models.TextField(blank=True)
    region_user = models.IntegerField()
    elevation_ft = models.IntegerField()
    record_modified = models.IntegerField()

    def __str__(self):
        return f"{self.af_name} ({self.af_code})"
