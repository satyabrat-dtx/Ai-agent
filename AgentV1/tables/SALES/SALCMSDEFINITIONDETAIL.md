# DB2ADMIN.SALCMSDEFINITIONDETAIL

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `SALCMSDEFINITIONCOMPANYCODE`, `SALCMSDEFINITIONNUMBERID`, `NUMBERLINEID`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 14311

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SALCMSDEFINITIONCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `SALCMSDEFINITIONNUMBERID` | DECIMAL(11,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `NUMBERLINEID` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 3 | `BREAKDOWNLIMIT` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 4 | `COMMISSIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 5 | `COMMISSIONVALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 6 | `COMMISSIONCURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 7 | `COMMISSIONSIGN` | CHAR(2) | NOT NULL |  |  |  |
| 8 | `CALCULATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CURRENCY_COMMISSIONCURRENCY` | `COMMISSIONCURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `SALCMSDEFINITIONDETAIL.COMMISSIONCURRENCYCODE = CURRENCY.CODE` |
| `SALESCOMMISSIONDEFINITION_COMMISSIONDETAIL` | `SALCMSDEFINITIONCOMPANYCODE`, `SALCMSDEFINITIONNUMBERID` | [`SALESCOMMISSIONDEFINITION`](../SALES/SALESCOMMISSIONDEFINITION.md) | `COMPANYCODE`, `NUMBERID` | RESTRICT | `SALCMSDEFINITIONDETAIL.SALCMSDEFINITIONCOMPANYCODE = SALESCOMMISSIONDEFINITION.COMPANYCODE AND SALCMSDEFINITIONDETAIL.SALCMSDEFINITIONNUMBERID = SALESCOMMISSIONDEFINITION.NUMBERID` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALCMSDEFINITIONDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SALCMSDEFINITIONCOMPANYCODE,
       t.SALCMSDEFINITIONNUMBERID,
       t.NUMBERLINEID,
       t.BREAKDOWNLIMIT,
       t.COMMISSIONTYPE,
       t.COMMISSIONVALUE,
       t.COMMISSIONCURRENCYCODE,
       t.COMMISSIONSIGN,
       t.CALCULATIONTYPE,
       t.AMOUNTCALCULATIONTYPE,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.SALCMSDEFINITIONDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
