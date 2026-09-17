# DB2ADMIN.PAYMENTMETHODIE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 122991

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `NOOFDAYS` | INTEGER | NOT NULL |  |  |  |
| 3 | `NOOFDAYS1` | INTEGER | NOT NULL |  |  |  |
| 4 | `NOOFDAYS2` | INTEGER | NOT NULL |  |  |  |
| 5 | `ADVANCE` | CHAR(1) |  |  |  |  |
| 6 | `ADVANCEBASEDONBASIC` | SMALLINT | NOT NULL |  |  |  |
| 7 | `AFTERMRN` | SMALLINT | NOT NULL |  |  |  |
| 8 | `PERCENTAGE1` | DECIMAL(9,5) | NOT NULL |  |  |  |
| 9 | `PERCENTAGE2` | DECIMAL(9,5) | NOT NULL |  |  |  |
| 10 | `LCRELATEDPAYMENT` | CHAR(1) |  |  |  |  |
| 11 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PAYMENTMETHODIE.COMPANYCODE = COMPANY.CODE` |
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PAYMENTMETHODIE.OWNINGCOMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PAYMENTMETHODIEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.NOOFDAYS,
       t.NOOFDAYS1,
       t.NOOFDAYS2,
       t.ADVANCE,
       t.ADVANCEBASEDONBASIC,
       t.AFTERMRN,
       t.PERCENTAGE1,
       t.PERCENTAGE2,
       t.LCRELATEDPAYMENT,
       t.OWNINGCOMPANYCODE
FROM   DB2ADMIN.PAYMENTMETHODIE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
