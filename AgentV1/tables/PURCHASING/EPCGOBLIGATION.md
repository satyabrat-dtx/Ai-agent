# DB2ADMIN.EPCGOBLIGATION

- **Module**: `PURCHASING` (low confidence — FK neighbourhood: 1 of 1 related tables are PURCHASING)
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `COMPANYCODE`, `EPCGAPPCODE`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 138257

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EPCGAPPCODE` | CHAR(30) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EPCGAPPLICATIONDATE` | DATE | NOT NULL |  |  |  |
| 3 | `EPCGFILENO` | CHAR(15) | NOT NULL |  |  |  |
| 4 | `EPCGFILEDATE` | DATE | NOT NULL |  |  |  |
| 5 | `EPCGLICENSENO` | CHAR(30) | NOT NULL |  |  |  |
| 6 | `EPCGLICENSEDATE` | DATE | NOT NULL |  |  |  |
| 7 | `FCCLEARANCEDATE` | DATE | NOT NULL |  |  |  |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `EPCGOBLIGATION.COMPANYCODE = COMPANY.CODE` |
| `EPCGAPPLICATION_EPCGAPP` | `COMPANYCODE`, `EPCGAPPCODE` | [`EPCGAPPLICATION`](../PURCHASING/EPCGAPPLICATION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EPCGOBLIGATION.COMPANYCODE = EPCGAPPLICATION.COMPANYCODE AND EPCGOBLIGATION.EPCGAPPCODE = EPCGAPPLICATION.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `EPCGOBLIGATION_OBLIINVOICELINE` | [`EPCGOBLIGATIONINVOICES`](../PURCHASING/EPCGOBLIGATIONINVOICES.md) | `EPCGOBLIGATIONCOMPANYCODE`, `EPCGOBLIGATIONEPCGAPPCODE` | `EPCGOBLIGATIONINVOICES.EPCGOBLIGATIONCOMPANYCODE = EPCGOBLIGATION.COMPANYCODE AND EPCGOBLIGATIONINVOICES.EPCGOBLIGATIONEPCGAPPCODE = EPCGOBLIGATION.EPCGAPPCODE` |

## Indexes

- `EPCGOBLIGATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EPCGAPPCODE,
       t.EPCGAPPLICATIONDATE,
       t.EPCGFILENO,
       t.EPCGFILEDATE,
       t.EPCGLICENSENO,
       t.EPCGLICENSEDATE,
       t.FCCLEARANCEDATE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.EPCGOBLIGATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
