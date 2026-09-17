# DB2ADMIN.ORDERPARTNERGST

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `CUSTOMERSUPPLIERCOMPANYCODE`, `CUSTOMERSUPPLIERTYPE`, `CUSTOMERSUPPLIERCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 129446

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CUSTOMERSUPPLIERCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 1 | `CUSTOMERSUPPLIERTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 2 | `CUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `GSTREGISTRATIONTYPE` | CHAR(1) |  |  |  |  |
| 4 | `ECOMMERCEOPERATOR` | SMALLINT | NOT NULL |  |  |  |
| 5 | `LATESTCOMPLIANCERATING` | CHAR(3) |  |  |  |  |
| 6 | `LATESTCOMPLIANCERATINGDATE` | DATE |  |  |  |  |
| 7 | `RCMAPPLICABLE` | CHAR(2) |  |  |  |  |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ORDERPARTNERGSTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CUSTOMERSUPPLIERCOMPANYCODE,
       t.CUSTOMERSUPPLIERTYPE,
       t.CUSTOMERSUPPLIERCODE,
       t.GSTREGISTRATIONTYPE,
       t.ECOMMERCEOPERATOR,
       t.LATESTCOMPLIANCERATING,
       t.LATESTCOMPLIANCERATINGDATE,
       t.RCMAPPLICABLE,
       t.ABSUNIQUEID,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.ORDERPARTNERGST t
FETCH FIRST 100 ROWS ONLY;
```
