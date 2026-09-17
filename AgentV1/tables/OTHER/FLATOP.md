# DB2ADMIN.FLATOP

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 42
- **Primary key**: `DIVISIONCODE`, `COMPANYCODE`, `UPLOADID`, `BELEGUNIQUE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 104037

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 1 | `COMPANYCODE` | CHAR(8) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `UPLOADID` | DECIMAL(9,0) | NOT NULL | PK | primary_key |  |
| 3 | `BELEGUNIQUE` | DECIMAL(15,0) | NOT NULL | PK | primary_key |  |
| 4 | `BELEGDATUM` | DATE |  |  |  |  |
| 5 | `BELEGNUMMER` | CHAR(20) |  |  |  |  |
| 6 | `BESTCASEDATUM` | DATE |  |  |  |  |
| 7 | `BESTCASEZAHLB` | DECIMAL(17,2) |  |  |  |  |
| 8 | `BESTCASEZAHLBLW` | DECIMAL(17,2) |  |  |  |  |
| 9 | `BETRAG` | DECIMAL(17,2) |  |  |  |  |
| 10 | `BETRAGLW` | DECIMAL(17,2) |  |  |  |  |
| 11 | `BUCHUNGSCODE` | CHAR(10) |  |  |  |  |
| 12 | `BUCHUNGSCODEBEZ` | VARCHAR(140) |  |  |  |  |
| 13 | `BUCHUNGSCODEBEZ2` | VARCHAR(140) |  |  |  |  |
| 14 | `BUCHUNGSDATUM` | DATE |  |  |  |  |
| 15 | `BUCHUNGSTEXT` | VARCHAR(140) |  |  |  |  |
| 16 | `FIRMENGRUPPE` | CHAR(3) |  |  |  |  |
| 17 | `FREMDBELEGDATUM` | DATE |  |  |  |  |
| 18 | `FREMDBELEGNUMMER` | CHAR(20) |  |  |  |  |
| 19 | `HAUPTBUCHBEZ` | VARCHAR(140) |  |  |  |  |
| 20 | `HAUPTBUCHBEZ2` | VARCHAR(140) |  |  |  |  |
| 21 | `HAUPTBUCH` | CHAR(10) |  |  |  |  |
| 22 | `KB` | CHAR(1) |  |  |  |  |
| 23 | `MAHNSTUFE` | INTEGER | NOT NULL |  |  |  |
| 24 | `NEBENBUCH` | CHAR(10) |  |  |  |  |
| 25 | `NEBENBUCHBEZ` | VARCHAR(140) |  |  |  |  |
| 26 | `NEBENBUCHBEZ2` | VARCHAR(140) |  |  |  |  |
| 27 | `NETTOFAELLIG` | DATE |  |  |  |  |
| 28 | `NETTOTAGE` | INTEGER | NOT NULL |  |  |  |
| 29 | `OPBETRAG` | DECIMAL(17,2) |  |  |  |  |
| 30 | `OPBETRAGLW` | DECIMAL(17,2) |  |  |  |  |
| 31 | `SH` | CHAR(1) |  |  |  |  |
| 32 | `SKONTOFAELLIG` | DATE |  |  |  |  |
| 33 | `SKONTOSATZ` | DECIMAL(5,2) |  |  |  |  |
| 34 | `SKONTOTAGE` | INTEGER | NOT NULL |  |  |  |
| 35 | `SONSTABZ` | DECIMAL(5,2) |  |  |  |  |
| 36 | `VALUTADATUM` | DATE |  |  |  |  |
| 37 | `WAEHRUNG` | CHAR(3) |  |  |  |  |
| 38 | `WORSTCASEDATUM` | DATE |  |  |  |  |
| 39 | `WORSTCASEZAHLB` | DECIMAL(17,2) |  |  |  |  |
| 40 | `WORSTCASEZAHLBLW` | DECIMAL(17,2) |  |  |  |  |
| 41 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FLATOPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.DIVISIONCODE,
       t.COMPANYCODE,
       t.UPLOADID,
       t.BELEGUNIQUE,
       t.BELEGDATUM,
       t.BELEGNUMMER,
       t.BESTCASEDATUM,
       t.BESTCASEZAHLB,
       t.BESTCASEZAHLBLW,
       t.BETRAG,
       t.BETRAGLW,
       t.BUCHUNGSCODE
FROM   DB2ADMIN.FLATOP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
