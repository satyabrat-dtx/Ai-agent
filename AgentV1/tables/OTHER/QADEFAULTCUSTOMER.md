# DB2ADMIN.QADEFAULTCUSTOMER

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `COMPANYCODE`, `CODECUSTOMERSUPPLIERTYPE`, `CODECUSTOMERSUPPLIERCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 85007

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODECUSTOMERSUPPLIERTYPE` | CHAR(1) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CODECUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 4 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 5 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 6 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `QADEFAULTCUSTOMER.COMPANYCODE = COMPANY.CODE` |
| `ORDERPARTNER_CODE` | `COMPANYCODE`, `CODECUSTOMERSUPPLIERTYPE`, `CODECUSTOMERSUPPLIERCODE` | [`ORDERPARTNER`](../CORE_MASTER/ORDERPARTNER.md) | `CUSTOMERSUPPLIERCOMPANYCODE`, `CUSTOMERSUPPLIERTYPE`, `CUSTOMERSUPPLIERCODE` | RESTRICT | `QADEFAULTCUSTOMER.COMPANYCODE = ORDERPARTNER.CUSTOMERSUPPLIERCOMPANYCODE AND QADEFAULTCUSTOMER.CODECUSTOMERSUPPLIERTYPE = ORDERPARTNER.CUSTOMERSUPPLIERTYPE AND QADEFAULTCUSTOMER.CODECUSTOMERSUPPLIERCODE = ORDERPARTNER.CUSTOMERSUPPLIERCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `QADEFAULTCUSTOMERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODECUSTOMERSUPPLIERTYPE,
       t.CODECUSTOMERSUPPLIERCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID
FROM   DB2ADMIN.QADEFAULTCUSTOMER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
