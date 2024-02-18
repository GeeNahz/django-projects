## Models
- [ ] User
- [x] Speaker
- [ ] Category
- [ ] Event
- [ ] EventMember
- [ ] Sponsorship
- [ ] Ticket
- [ ] EventResource
## Relationships
- [ ] Category => one-to-many => Event
- [ ] Event => one-to-many => attendees (User) |> EventMember
- [ ] Event => one-to-many => Sponsor
- [ ] Event => one-to-many => Ticket
- [ ] Event => one-to-many => Resource
- [ ] Speaker (profile) => one-to-one => User

## Functions
- [ ] Event management
    - [ ] Create, Edit, and Delete events
    - [ ] Manage even attendance through RSVPs and registrations
    - [ ] Assign roles to users such as organiser, speaker, attendee
- [ ] User management
    - [ ] Create user accounts with profiles
    - [ ] Manage user information and roles
    - [ ] Allow users to registrer for events and manage their attendance status
- [ ] Category management
    - [ ] Create, Edit, and Delete categories
- [ ] Speaker management
    - [ ] Create speaker profiles and bios, websites, and company information
    - [ ] Link speakers to event they are presenting at
- [ ] Sponsorship management
    - [ ] Add, Edit, Remove, sponsorship
    - [ ] Manage sponsorhip details such as details, logos, and descriptions
    - [ ] Track sponsorship for each event
- [ ] Ticket management
    - [ ] Create and manage event tickets with prices, currencies, and sale dates
    - [ ] Track ticket sales and attendee registrations
- [ ] Event Resource management
    - [ ] Upload and manage event resources like presentations, recordings, and documents
    - [ ] Link resources to specific events for easy access

## Additional functions
- [ ] Dashboard for admin and attendees (user dashboard essentially)
- [ ] User signup/registration
- [ ] Send emails to organisers, attendees, and speakers
    - [ ] Organisers: How many tickets sales have been made, tickets sold out, reminder for start of events...
    - [ ] Attendees: Ticket with QR code, start of event...
    - [ ] Speakers: start of event...
- [ ] Generate reports on event attendance, registrations, and ticket sales (could cover for the Organisers part above)
- [ ] Search and filter events by category, date, and other criteria
