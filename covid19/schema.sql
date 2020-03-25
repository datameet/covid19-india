create table covid19_thehindu_entry (
    id serial primary key,
    timestamp timestamp
);
create index covid19_thehindu_entry_timestamp_idx on covid19_thehindu_entry(timestamp);


create table covid19_thehindu (
    id serial primary key,
    entry_id integer references covid19_thehindu_entry,
    state_code char(2),
    confirmed int,
    active int,
    recovered int,
    deaths int,
    indians int,
    foreigners int
);

