create table if not exists users
(
    User_name            varchar(255) not null
        primary key,
    First_name           varchar(255) null,
    Last_name            varchar(255) null,
    email                varchar(255) null,
    age                  int          null,
    Academic_institution varchar(255) null,
    Gender               varchar(255) null,
    City                 varchar(255) null,
    about_me             varchar(400) null,
    password             varchar(120) null
);

create table if not exists training
(
    trainingID             int auto_increment
        primary key,
    Workout_type           varchar(255) null,
    location_lat           double       null,
    location_lng           double       null,
    Gender                 varchar(255) null,
    workout_date           date         null,
    workout_time           time         null,
    number_of_participants int          null,
    user_host              varchar(255) null,
    description            varchar(255) null,
    duration               int          null,
    constraint owner___fk
        foreign key (user_host) references users (User_name)
);

create table if not exists participant
(
    participant varchar(255) not null,
    training    int          not null,
    primary key (participant, training),
    constraint participant_training__fk
        foreign key (training) references training (trainingID),
    constraint participant_users__fk
        foreign key (participant) references users (User_name)
);

