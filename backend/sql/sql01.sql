CREATE TABLE learner
    (
        id  bigserial NOT NULL,
        code bigint,
        name text,
        email text,
        search_str text,
        level_id bigint,
        created_at timestamp with time zone NOT NULL DEFAULT now(),
        created_by bigint,
        modified_at timestamp with time zone,
        modified_by bigint,
        deleted_at timestamp with time zone,
        deleted_by bigint,
        active boolean DEFAULT TRUE,
        CONSTRAINT pkey_learner PRIMARY KEY (id)
    );
create unique index learner_unique_code on learner (code) where active is true;
create unique index learner_unique_name on learner (name) where active is true;
create unique index learner_unique_email on learner (email) where active is true;


CREATE TABLE level
    (
        id  bigserial NOT NULL,
        code int8,
        name text,
        search_str text,
        created_at timestamp with time zone NOT NULL DEFAULT now(),
        created_by bigint,
        modified_at timestamp with time zone,
        modified_by bigint,
        deleted_at timestamp with time zone,
        deleted_by bigint,
        active boolean DEFAULT TRUE,
        CONSTRAINT pkey_level PRIMARY KEY (id)
    );
create unique index level_unique_code on level (code) where active is true;
create unique index level_unique_name on level (name) where active is true;
insert into level(code, name) values (1, 'N1'), (2, 'N2'), (3, 'N3'), (4, 'N4'), (5, 'N5');