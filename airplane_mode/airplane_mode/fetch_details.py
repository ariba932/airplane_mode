import frappe

@frappe.whitelist()
def get_airplanes_by_airline(airline):
    airplanes = frappe.db.get_list('Airplane', filters={'airline': airline}, fields=['name'])
    return [airplane.name for airplane in airplanes]


@frappe.whitelist()
def get_available_flights(crew_member):
    # Get the airline of the crew member
    airline = frappe.db.get_value('Crew Member', crew_member, 'airline')
    print("Crew airline-",airline)
    # Get the list of flights the crew member is already assigned to
    assigned_flights = frappe.db.get_list('Crew Flight Register', filters={
        'crew_member': crew_member,
        'status': ['in', ['Assigned', 'Pending']]
    }, fields=['flight','flight_date'])

    print("assigned -flight ", assigned_flights)

    # Get the list of available planes for the airlines
    planes = frappe.db.get_list('Airplane', filters={'airline':airline }, fields=['name'])
    
    assigned_flight_ids = [flight.flight for flight in assigned_flights]
    assigned_dates = [flight.flight_date for flight in assigned_flights]
    assigned_planes =[plane.name for plane in planes]
  
    print("fetched flight -dates", assigned_dates)
    print("List of planes", assigned_planes)
    
    # Get the list of available flights that do not clash with existing assignments and are from the same airline
    available_flights = frappe.db.get_list('Airplane Flight', filters={
        'name': ['not in', assigned_flight_ids],
        'date': ['not in', assigned_dates],
        'airplane': ['in',assigned_planes]
    }, fields=['name'])

    print("list of available -", available_flights)
    
    return [flight.name for flight in available_flights]

