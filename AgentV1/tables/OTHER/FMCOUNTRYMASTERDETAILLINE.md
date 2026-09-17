# DB2ADMIN.FMCOUNTRYMASTERDETAILLINE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `FMCNYMASTERDETAILCOMPANYCODE`, `FMCNYMDETAILSCHEMETYPECODE`, `FMCNYMASTERDETAILCOUNTRYCODE`, `FMCNYMDETAILEFFECTIVEDATEFROM`, `TARIFFCODE`, `EFFECTIVEFROMDATE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 121870

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FMCNYMASTERDETAILCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FMCNYMDETAILSCHEMETYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `FMCNYMASTERDETAILCOUNTRYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `FMCNYMDETAILEFFECTIVEDATEFROM` | DATE | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `TARIFFCODE` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `RATE` | DECIMAL(18,5) |  |  |  |  |
| 6 | `EFFECTIVEFROMDATE` | DATE | NOT NULL | PK | primary_key |  |
| 7 | `EFFECTIVETODATE` | DATE |  |  |  |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FMCOUNTRYMASTERDETAIL_DETAIL` | `FMCNYMASTERDETAILCOMPANYCODE`, `FMCNYMDETAILSCHEMETYPECODE`, `FMCNYMASTERDETAILCOUNTRYCODE`, `FMCNYMDETAILEFFECTIVEDATEFROM` | [`FMCOUNTRYMASTERDETAIL`](../OTHER/FMCOUNTRYMASTERDETAIL.md) | `COMPANYCODE`, `SCHEMETYPECODE`, `COUNTRYCODE`, `EFFECTIVEDATEFROM` | RESTRICT | `FMCOUNTRYMASTERDETAILLINE.FMCNYMASTERDETAILCOMPANYCODE = FMCOUNTRYMASTERDETAIL.COMPANYCODE AND FMCOUNTRYMASTERDETAILLINE.FMCNYMDETAILSCHEMETYPECODE = FMCOUNTRYMASTERDETAIL.SCHEMETYPECODE AND FMCOUNTRYMASTERDETAILLINE.FMCNYMASTERDETAILCOUNTRYCODE = FMCOUNTRYMASTERDETAIL.COUNTRYCODE AND FMCOUNTRYMASTERDETAILLINE.FMCNYMDETAILEFFECTIVEDATEFROM = FMCOUNTRYMASTERDETAIL.EFFECTIVEDATEFROM` |
| `TARIFF_TARIFF` | `TARIFFCODE` | [`TARIFF`](../CORE_MASTER/TARIFF.md) | `CODE` | RESTRICT | `FMCOUNTRYMASTERDETAILLINE.TARIFFCODE = TARIFF.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FMCOUNTRYMASTERDETAILLINEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FMCNYMASTERDETAILCOMPANYCODE,
       t.FMCNYMDETAILSCHEMETYPECODE,
       t.FMCNYMASTERDETAILCOUNTRYCODE,
       t.FMCNYMDETAILEFFECTIVEDATEFROM,
       t.TARIFFCODE,
       t.RATE,
       t.EFFECTIVEFROMDATE,
       t.EFFECTIVETODATE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.FMCOUNTRYMASTERDETAILLINE t
FETCH FIRST 100 ROWS ONLY;
```
