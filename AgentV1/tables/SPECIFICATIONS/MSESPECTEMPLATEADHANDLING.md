# DB2ADMIN.MSESPECTEMPLATEADHANDLING

- **Module**: `SPECIFICATIONS` (medium confidence — table name starts with 'MSE')
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `MSESPECTEMPLATECOMPANYCODE`, `MSESPECIFICATIONTEMPLATECODE`, `SEQUENCE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 99070

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `MSESPECTEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `MSESPECIFICATIONTEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SEQUENCE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `ADENTITY` | CHAR(2) | NOT NULL |  |  |  |
| 4 | `ADNAME` | CHAR(50) | NOT NULL |  |  |  |
| 5 | `ADFIELDNAME` | VARCHAR(120) | NOT NULL |  |  |  |
| 6 | `OPERATOR` | CHAR(2) | NOT NULL |  |  |  |
| 7 | `DATATYPE` | INTEGER | NOT NULL |  |  |  |
| 8 | `VALUESTRING` | VARCHAR(250) |  |  |  |  |
| 9 | `VALUEINT` | INTEGER | NOT NULL |  |  |  |
| 10 | `VALUEBOOLEAN` | SMALLINT | NOT NULL |  |  |  |
| 11 | `VALUEDATE` | DATE |  |  |  |  |
| 12 | `VALUEDECIMAL` | DECIMAL(18,5) |  |  |  |  |
| 13 | `VALUELONG` | BIGINT | NOT NULL |  |  |  |
| 14 | `VALUETIME` | TIME |  |  |  |  |
| 15 | `VALUETIMESTAMP` | TIMESTAMP |  |  |  |  |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 17 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 18 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 19 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 20 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 21 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 22 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `MSESPECIFICATIONTEMPLATE_ADHANDLING` | `MSESPECTEMPLATECOMPANYCODE`, `MSESPECIFICATIONTEMPLATECODE` | [`MSESPECIFICATIONTEMPLATE`](../SPECIFICATIONS/MSESPECIFICATIONTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `MSESPECTEMPLATEADHANDLING.MSESPECTEMPLATECOMPANYCODE = MSESPECIFICATIONTEMPLATE.COMPANYCODE AND MSESPECTEMPLATEADHANDLING.MSESPECIFICATIONTEMPLATECODE = MSESPECIFICATIONTEMPLATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `MSESPECTEMPLATEADHANDLINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.MSESPECTEMPLATECOMPANYCODE,
       t.MSESPECIFICATIONTEMPLATECODE,
       t.SEQUENCE,
       t.ADENTITY,
       t.ADNAME,
       t.ADFIELDNAME,
       t.OPERATOR,
       t.DATATYPE,
       t.VALUESTRING,
       t.VALUEINT,
       t.VALUEBOOLEAN,
       t.VALUEDATE
FROM   DB2ADMIN.MSESPECTEMPLATEADHANDLING t
FETCH FIRST 100 ROWS ONLY;
```
