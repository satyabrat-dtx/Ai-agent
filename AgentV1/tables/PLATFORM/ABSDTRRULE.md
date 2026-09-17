# DB2ADMIN.ABSDTRRULE

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 28
- **Primary key**: `ABSDTRENTITYGROUPFAMILY`, `ABSDTRENTITYREFERENCEDENTITY`, `ABSDTRENTITYDTRPKTOKEN`, `RULEUNIQUEID`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 96783

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSDTRENTITYGROUPFAMILY` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ABSDTRENTITYREFERENCEDENTITY` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `RULEUNIQUEID` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `RULEROW` | INTEGER | NOT NULL |  |  |  |
| 4 | `RULEROWDETAIL` | INTEGER | NOT NULL |  |  |  |
| 5 | `RULETYPE` | INTEGER | NOT NULL |  |  |  |
| 6 | `INPUTUNIQUEIDENT` | INTEGER | NOT NULL |  |  |  |
| 7 | `FIELDNAME` | VARCHAR(120) | NOT NULL |  |  |  |
| 8 | `FIELDOPERATOR` | CHAR(9) | NOT NULL |  |  |  |
| 9 | `NULLVALUE` | SMALLINT | NOT NULL |  |  |  |
| 10 | `VALUESTRING` | VARCHAR(250) |  |  |  |  |
| 11 | `VALUEINT` | INTEGER | NOT NULL |  |  |  |
| 12 | `VALUEBOOLEAN` | SMALLINT | NOT NULL |  |  |  |
| 13 | `VALUEDATE` | DATE |  |  |  |  |
| 14 | `VALUEDECIMAL` | DECIMAL(18,5) |  |  |  |  |
| 15 | `VALUELONG` | BIGINT | NOT NULL |  |  |  |
| 16 | `VALUETIME` | TIME |  |  |  |  |
| 17 | `VALUETIMESTAMP` | TIMESTAMP |  |  |  |  |
| 18 | `DATATYPE` | INTEGER | NOT NULL |  |  |  |
| 19 | `RESOLVERPLYCODE` | CHAR(20) |  |  |  |  |
| 20 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 21 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 22 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 23 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 24 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 25 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 26 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 27 | `ABSDTRENTITYDTRPKTOKEN` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSDTRENTITY_DTRRULE` | `ABSDTRENTITYGROUPFAMILY`, `ABSDTRENTITYREFERENCEDENTITY`, `ABSDTRENTITYDTRPKTOKEN` | [`ABSDTRENTITY`](../PLATFORM/ABSDTRENTITY.md) | `GROUPFAMILY`, `REFERENCEDENTITY`, `DTRPKTOKEN` | RESTRICT | `ABSDTRRULE.ABSDTRENTITYGROUPFAMILY = ABSDTRENTITY.GROUPFAMILY AND ABSDTRRULE.ABSDTRENTITYREFERENCEDENTITY = ABSDTRENTITY.REFERENCEDENTITY AND ABSDTRRULE.ABSDTRENTITYDTRPKTOKEN = ABSDTRENTITY.DTRPKTOKEN` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSDTRRULEUID` (ABSUNIQUEID)
- `ABSDTRRULEIDX01` (ABSDTRENTITYGROUPFAMILY, ABSDTRENTITYREFERENCEDENTITY, RULETYPE, RULEROW, RULEROWDETAIL)

## Starter query

```sql
SELECT t.ABSDTRENTITYGROUPFAMILY,
       t.ABSDTRENTITYREFERENCEDENTITY,
       t.RULEUNIQUEID,
       t.RULEROW,
       t.RULEROWDETAIL,
       t.RULETYPE,
       t.INPUTUNIQUEIDENT,
       t.FIELDNAME,
       t.FIELDOPERATOR,
       t.NULLVALUE,
       t.VALUESTRING,
       t.VALUEINT
FROM   DB2ADMIN.ABSDTRRULE t
FETCH FIRST 100 ROWS ONLY;
```
