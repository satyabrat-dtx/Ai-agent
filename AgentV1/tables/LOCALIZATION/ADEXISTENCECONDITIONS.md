# DB2ADMIN.ADEXISTENCECONDITIONS

- **Module**: `LOCALIZATION` (low confidence — FK neighbourhood: 1 of 1 related tables are LOCALIZATION)
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `ADADDITIONALDATAENTITYNAME`, `ADADDITIONALDATANAME`, `SEQUENCE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 6784

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ADADDITIONALDATAENTITYNAME` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ADADDITIONALDATANAME` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SEQUENCE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `FIELDNAMEFIELDNAME` | VARCHAR(120) |  | FK | foreign_key |  |
| 4 | `COMPAREOP` | INTEGER | NOT NULL |  |  |  |
| 5 | `VALUE` | CHAR(50) | NOT NULL |  |  |  |
| 6 | `CONCAT` | INTEGER | NOT NULL |  |  |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ADADDITIONALDATA_EXISTENCECONDITIONS` | `ADADDITIONALDATAENTITYNAME`, `ADADDITIONALDATANAME` | [`ADADDITIONALDATA`](../CORE_MASTER/ADADDITIONALDATA.md) | `ENTITYNAME`, `NAME` | RESTRICT | `ADEXISTENCECONDITIONS.ADADDITIONALDATAENTITYNAME = ADADDITIONALDATA.ENTITYNAME AND ADEXISTENCECONDITIONS.ADADDITIONALDATANAME = ADADDITIONALDATA.NAME` |
| `ADATTRIBUTE_FIELDNAME` | `ADADDITIONALDATAENTITYNAME`, `FIELDNAMEFIELDNAME` | [`ADATTRIBUTE`](../LOCALIZATION/ADATTRIBUTE.md) | `ENTITYNAME`, `FIELDNAME` | RESTRICT | `ADEXISTENCECONDITIONS.ADADDITIONALDATAENTITYNAME = ADATTRIBUTE.ENTITYNAME AND ADEXISTENCECONDITIONS.FIELDNAMEFIELDNAME = ADATTRIBUTE.FIELDNAME` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ADEXISTENCECONDITIONSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ADADDITIONALDATAENTITYNAME,
       t.ADADDITIONALDATANAME,
       t.SEQUENCE,
       t.FIELDNAMEFIELDNAME,
       t.COMPAREOP,
       t.VALUE,
       t.CONCAT,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ADEXISTENCECONDITIONS t
FETCH FIRST 100 ROWS ONLY;
```
