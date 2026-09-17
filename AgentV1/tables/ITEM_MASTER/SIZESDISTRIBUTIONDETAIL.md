# DB2ADMIN.SIZESDISTRIBUTIONDETAIL

- **Module**: `ITEM_MASTER` (low confidence — FK neighbourhood: 1 of 1 related tables are ITEM_MASTER)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `SIZEDISTRSIZETYPECOMPANYCODE`, `SIZESDISTRIBUTIONCODE`, `SIZECODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 97099

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SIZEDISTRSIZETYPECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `SIZESDISTRIBUTIONCODE` | CHAR(30) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SIZECODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 3 | `DISTRIBUTION` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 4 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 11 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SIZESDISTRIBUTIONDETAIL.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `SIZESDISTRIBUTION_DETAILS` | `SIZEDISTRSIZETYPECOMPANYCODE`, `SIZESDISTRIBUTIONCODE` | [`SIZESDISTRIBUTION`](../ITEM_MASTER/SIZESDISTRIBUTION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SIZESDISTRIBUTIONDETAIL.SIZEDISTRSIZETYPECOMPANYCODE = SIZESDISTRIBUTION.COMPANYCODE AND SIZESDISTRIBUTIONDETAIL.SIZESDISTRIBUTIONCODE = SIZESDISTRIBUTION.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SIZESDISTRIBUTIONDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SIZEDISTRSIZETYPECOMPANYCODE,
       t.SIZESDISTRIBUTIONCODE,
       t.SIZECODE,
       t.DISTRIBUTION,
       t.OWNINGCOMPANYCODE,
       t.ABSUNIQUEID,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.SIZESDISTRIBUTIONDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
