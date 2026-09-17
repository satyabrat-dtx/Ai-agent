# DB2ADMIN.LEARNINGCURVE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 27
- **Primary key**: `CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 208108

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(6) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 2 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 3 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 4 | `NUMBEROFHOURS1` | INTEGER | NOT NULL |  |  |  |
| 5 | `EFFICIENCYPERCENT1` | DECIMAL(4,1) |  |  |  |  |
| 6 | `NUMBEROFHOURS2` | INTEGER | NOT NULL |  |  |  |
| 7 | `EFFICIENCYPERCENT2` | DECIMAL(4,1) |  |  |  |  |
| 8 | `NUMBEROFHOURS3` | INTEGER | NOT NULL |  |  |  |
| 9 | `EFFICIENCYPERCENT3` | DECIMAL(4,1) |  |  |  |  |
| 10 | `NUMBEROFHOURS4` | INTEGER | NOT NULL |  |  |  |
| 11 | `EFFICIENCYPERCENT4` | DECIMAL(4,1) |  |  |  |  |
| 12 | `NUMBEROFHOURS5` | INTEGER | NOT NULL |  |  |  |
| 13 | `EFFICIENCYPERCENT5` | DECIMAL(4,1) |  |  |  |  |
| 14 | `NUMBEROFHOURS6` | INTEGER | NOT NULL |  |  |  |
| 15 | `EFFICIENCYPERCENT6` | DECIMAL(4,1) |  |  |  |  |
| 16 | `NUMBEROFHOURS7` | INTEGER | NOT NULL |  |  |  |
| 17 | `EFFICIENCYPERCENT7` | DECIMAL(4,1) |  |  |  |  |
| 18 | `NUMBEROFHOURS8` | INTEGER | NOT NULL |  |  |  |
| 19 | `EFFICIENCYPERCENT8` | DECIMAL(4,1) |  |  |  |  |
| 20 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 21 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 22 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 23 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 24 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 25 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 26 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LEARNINGCURVEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.NUMBEROFHOURS1,
       t.EFFICIENCYPERCENT1,
       t.NUMBEROFHOURS2,
       t.EFFICIENCYPERCENT2,
       t.NUMBEROFHOURS3,
       t.EFFICIENCYPERCENT3,
       t.NUMBEROFHOURS4,
       t.EFFICIENCYPERCENT4
FROM   DB2ADMIN.LEARNINGCURVE t
FETCH FIRST 100 ROWS ONLY;
```
