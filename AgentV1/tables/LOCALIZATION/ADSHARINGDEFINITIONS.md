# DB2ADMIN.ADSHARINGDEFINITIONS

- **Module**: `LOCALIZATION` (low confidence — FK neighbourhood: 1 of 1 related tables are LOCALIZATION)
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `ADADDITIONALDATAENTITYNAME`, `ADADDITIONALDATANAME`, `FIELDNAMEFIELDNAME`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 3459

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ADADDITIONALDATAENTITYNAME` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ADADDITIONALDATANAME` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `FIELDNAMEFIELDNAME` | VARCHAR(120) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `DUMMYBUL` | SMALLINT | NOT NULL |  |  |  |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ADADDITIONALDATA_SHARINGDEFINITIONS` | `ADADDITIONALDATAENTITYNAME`, `ADADDITIONALDATANAME` | [`ADADDITIONALDATA`](../CORE_MASTER/ADADDITIONALDATA.md) | `ENTITYNAME`, `NAME` | RESTRICT | `ADSHARINGDEFINITIONS.ADADDITIONALDATAENTITYNAME = ADADDITIONALDATA.ENTITYNAME AND ADSHARINGDEFINITIONS.ADADDITIONALDATANAME = ADADDITIONALDATA.NAME` |
| `ADATTRIBUTE_FIELDNAME` | `ADADDITIONALDATAENTITYNAME`, `FIELDNAMEFIELDNAME` | [`ADATTRIBUTE`](../LOCALIZATION/ADATTRIBUTE.md) | `ENTITYNAME`, `FIELDNAME` | RESTRICT | `ADSHARINGDEFINITIONS.ADADDITIONALDATAENTITYNAME = ADATTRIBUTE.ENTITYNAME AND ADSHARINGDEFINITIONS.FIELDNAMEFIELDNAME = ADATTRIBUTE.FIELDNAME` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ADSHARINGDEFINITIONSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ADADDITIONALDATAENTITYNAME,
       t.ADADDITIONALDATANAME,
       t.FIELDNAMEFIELDNAME,
       t.DUMMYBUL,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ADSHARINGDEFINITIONS t
FETCH FIRST 100 ROWS ONLY;
```
