# DB2ADMIN.NETCOMPANYSETUP

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'NET')
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 122670

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `COSTCURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 2 | `FINANCESYSTEM` | CHAR(2) | NOT NULL |  |  |  |
| 3 | `POSTINGPOLICYREFERENCECODE` | CHAR(20) |  |  |  |  |
| 4 | `PURCHASEINVOICEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 5 | `GLMASTERLOGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 7 | `GLGROUPBYTAX` | SMALLINT | NOT NULL |  |  |  |
| 8 | `QCCHECKREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 9 | `LOGFORALLENTITIES` | SMALLINT | NOT NULL |  |  |  |
| 10 | `TCSDIVISION` | SMALLINT | NOT NULL |  |  |  |
| 11 | `TCSAPPLICABLE` | SMALLINT | NOT NULL |  |  |  |
| 12 | `TDSEXCEMPTIONCALREQ` | SMALLINT | NOT NULL |  |  |  |
| 13 | `INTERCOMPMRNINPLANTINVOICE` | SMALLINT | NOT NULL |  |  |  |
| 14 | `INDIANISATIONREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 15 | `MRNPOSTINGBEFOREQC` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `NETCOMPANYSETUP.COMPANYCODE = COMPANY.CODE` |
| `CURRENCY_COSTCURRENCY` | `COSTCURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `NETCOMPANYSETUP.COSTCURRENCYCODE = CURRENCY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `NETCOMPANYSETUPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.COSTCURRENCYCODE,
       t.FINANCESYSTEM,
       t.POSTINGPOLICYREFERENCECODE,
       t.PURCHASEINVOICEREQUIRED,
       t.GLMASTERLOGMANAGEMENT,
       t.ABSUNIQUEID,
       t.GLGROUPBYTAX,
       t.QCCHECKREQUIRED,
       t.LOGFORALLENTITIES,
       t.TCSDIVISION,
       t.TCSAPPLICABLE
FROM   DB2ADMIN.NETCOMPANYSETUP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
