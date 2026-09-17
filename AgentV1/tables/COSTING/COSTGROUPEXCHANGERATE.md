# DB2ADMIN.COSTGROUPEXCHANGERATE

- **Module**: `COSTING` (high confidence — table name starts with 'COST')
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `COSTGROUPCOMPANYCODE`, `COSTGROUPCODE`, `CURRENCYCODE`, `REFERENCEDCURRENCYCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 17119

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COSTGROUPCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `COSTGROUPCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CURRENCYCODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `REFERENCEDCURRENCYCODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `EXCHANGERATE` | DECIMAL(28,15) | NOT NULL |  |  |  |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 10 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 11 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COSTGROUP_COSTINGEXCHANGE` | `COSTGROUPCOMPANYCODE`, `COSTGROUPCODE` | [`COSTGROUP`](../COSTING/COSTGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `COSTGROUPEXCHANGERATE.COSTGROUPCOMPANYCODE = COSTGROUP.COMPANYCODE AND COSTGROUPEXCHANGERATE.COSTGROUPCODE = COSTGROUP.CODE` |
| `CURRENCY_CURRENCY` | `CURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `COSTGROUPEXCHANGERATE.CURRENCYCODE = CURRENCY.CODE` |
| `CURRENCY_REFERENCEDCURRENCY` | `REFERENCEDCURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `COSTGROUPEXCHANGERATE.REFERENCEDCURRENCYCODE = CURRENCY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `COSTGROUPEXCHANGERATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COSTGROUPCOMPANYCODE,
       t.COSTGROUPCODE,
       t.CURRENCYCODE,
       t.REFERENCEDCURRENCYCODE,
       t.EXCHANGERATE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.COSTGROUPEXCHANGERATE t
FETCH FIRST 100 ROWS ONLY;
```
