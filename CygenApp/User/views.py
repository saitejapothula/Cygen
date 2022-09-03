from .User_Crud.User_Register import RegisterAPI
from .User_Crud.User_appointment import CreateUserAppointment
from .User_Crud.get_appointments import GetAppointments
from .User_Crud.get_user_details import GetUserList
# Create your views here.
RegisterAPI()
GetUserList()
CreateUserAppointment()
GetAppointments()