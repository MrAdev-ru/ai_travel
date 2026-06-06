-- AI Travel Assistant - PostgreSQL Database Schema
-- Generated for university final project documentation
-- Note: Django migrations are the source of truth; this schema mirrors the models.

-- =============================================================================
-- Django Built-in: auth_user (User model)
-- =============================================================================
CREATE TABLE IF NOT EXISTS auth_user (
    id              BIGSERIAL PRIMARY KEY,
    password        VARCHAR(128) NOT NULL,
    last_login      TIMESTAMP WITH TIME ZONE,
    is_superuser    BOOLEAN NOT NULL DEFAULT FALSE,
    username        VARCHAR(150) NOT NULL UNIQUE,
    first_name      VARCHAR(150) NOT NULL DEFAULT '',
    last_name       VARCHAR(150) NOT NULL DEFAULT '',
    email           VARCHAR(254) NOT NULL DEFAULT '',
    is_staff        BOOLEAN NOT NULL DEFAULT FALSE,
    is_active       BOOLEAN NOT NULL DEFAULT TRUE,
    date_joined     TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS auth_user_username_idx ON auth_user (username);

-- =============================================================================
-- TranslationHistory - stores user translation records
-- =============================================================================
CREATE TABLE IF NOT EXISTS translations_translationhistory (
    id                  BIGSERIAL PRIMARY KEY,
    user_id             BIGINT NOT NULL REFERENCES auth_user(id) ON DELETE CASCADE,
    source_text         TEXT NOT NULL,
    translated_text     TEXT NOT NULL,
    source_language     VARCHAR(10) NOT NULL,
    target_language     VARCHAR(10) NOT NULL,
    detected_language   VARCHAR(10) NOT NULL DEFAULT '',
    created_at          TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS translations_history_user_idx
    ON translations_translationhistory (user_id);
CREATE INDEX IF NOT EXISTS translations_history_created_idx
    ON translations_translationhistory (created_at DESC);

-- =============================================================================
-- FavoriteTranslation - user-saved favorite translations
-- =============================================================================
CREATE TABLE IF NOT EXISTS translations_favoritetranslation (
    id                  BIGSERIAL PRIMARY KEY,
    user_id             BIGINT NOT NULL REFERENCES auth_user(id) ON DELETE CASCADE,
    source_text         TEXT NOT NULL,
    translated_text     TEXT NOT NULL,
    source_language     VARCHAR(10) NOT NULL,
    target_language     VARCHAR(10) NOT NULL,
    history_id          BIGINT REFERENCES translations_translationhistory(id) ON DELETE SET NULL,
    created_at          TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    UNIQUE (user_id, source_text, target_language)
);

CREATE INDEX IF NOT EXISTS translations_favorite_user_idx
    ON translations_favoritetranslation (user_id);

-- =============================================================================
-- PhraseCategory - travel phrasebook categories
-- =============================================================================
CREATE TABLE IF NOT EXISTS phrasebook_phrasecategory (
    id          BIGSERIAL PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    slug        VARCHAR(50) NOT NULL UNIQUE,
    icon        VARCHAR(50) NOT NULL,
    description TEXT NOT NULL DEFAULT '',
    "order"     INTEGER NOT NULL DEFAULT 0 CHECK ("order" >= 0)
);

CREATE INDEX IF NOT EXISTS phrasebook_category_slug_idx
    ON phrasebook_phrasecategory (slug);

-- =============================================================================
-- Phrase - individual travel phrases with JSON translations
-- =============================================================================
CREATE TABLE IF NOT EXISTS phrasebook_phrase (
    id              BIGSERIAL PRIMARY KEY,
    category_id     BIGINT NOT NULL REFERENCES phrasebook_phrasecategory(id) ON DELETE CASCADE,
    source_text     VARCHAR(500) NOT NULL,
    source_language VARCHAR(10) NOT NULL DEFAULT 'en',
    translations    JSONB NOT NULL DEFAULT '{}',
    pronunciation   VARCHAR(500) NOT NULL DEFAULT '',
    "order"         INTEGER NOT NULL DEFAULT 0 CHECK ("order" >= 0)
);

CREATE INDEX IF NOT EXISTS phrasebook_phrase_category_idx
    ON phrasebook_phrase (category_id);

-- =============================================================================
-- Entity Relationship Summary
-- =============================================================================
-- auth_user (1) ----< (N) translations_translationhistory
-- auth_user (1) ----< (N) translations_favoritetranslation
-- translations_translationhistory (1) ----< (N) translations_favoritetranslation [optional FK]
-- phrasebook_phrasecategory (1) ----< (N) phrasebook_phrase
