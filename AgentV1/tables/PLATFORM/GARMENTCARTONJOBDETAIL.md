# DB2ADMIN.GARMENTCARTONJOBDETAIL

- **Module**: `PLATFORM` (low confidence — FK neighbourhood: 1 of 1 related tables are PLATFORM)
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `GARMENTCARTONHEADERCOMPANYCODE`, `GARMENTCARTONHEADERNUMBERID`, `SUBMITTEBJOBJOBNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 215054

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `GARMENTCARTONHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `GARMENTCARTONHEADERNUMBERID` | DECIMAL(11,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL |  | audit |  |
| 3 | `SUBMITTEBJOBJOBNUMBER` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 5 | `DESCRIPTION` | CHAR(100) |  |  | description |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSSUBMITTEDJOB_SUBMITTEBJOB` | `SUBMITTEBJOBJOBNUMBER` | [`ABSSUBMITTEDJOB`](../PLATFORM/ABSSUBMITTEDJOB.md) | `JOBNUMBER` | RESTRICT | `GARMENTCARTONJOBDETAIL.SUBMITTEBJOBJOBNUMBER = ABSSUBMITTEDJOB.JOBNUMBER` |
| `GARMENTCARTONHEADER_CHILDSUBMITTEDJOB` | `GARMENTCARTONHEADERCOMPANYCODE`, `GARMENTCARTONHEADERNUMBERID` | [`GARMENTCARTONHEADER`](../CORE_MASTER/GARMENTCARTONHEADER.md) | `COMPANYCODE`, `NUMBERID` | RESTRICT | `GARMENTCARTONJOBDETAIL.GARMENTCARTONHEADERCOMPANYCODE = GARMENTCARTONHEADER.COMPANYCODE AND GARMENTCARTONJOBDETAIL.GARMENTCARTONHEADERNUMBERID = GARMENTCARTONHEADER.NUMBERID` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `GARMENTCARTONJOBDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.GARMENTCARTONHEADERCOMPANYCODE,
       t.GARMENTCARTONHEADERNUMBERID,
       t.CREATIONTIMESTAMP,
       t.SUBMITTEBJOBJOBNUMBER,
       t.STATUS,
       t.DESCRIPTION,
       t.ABSUNIQUEID
FROM   DB2ADMIN.GARMENTCARTONJOBDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
