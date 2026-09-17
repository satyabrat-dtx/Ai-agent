# DB2ADMIN.REPLENISHMENTCUSTOMIZATION

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 29879

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONLEVEL` | CHAR(2) | NOT NULL |  |  |  |
| 2 | `REQUISITIONTEMPLATELEVEL` | CHAR(2) | NOT NULL |  |  |  |
| 3 | `APPLICANTLEVEL` | CHAR(2) | NOT NULL |  |  |  |
| 4 | `DELIVERYDATELEVEL` | CHAR(2) | NOT NULL |  |  |  |
| 5 | `COSTCENTERLEVEL` | CHAR(2) | NOT NULL |  |  |  |
| 6 | `PURCHASEORDERTEMPLATELEVEL` | CHAR(2) | NOT NULL |  |  |  |
| 7 | `PURCHASEORDERLINETEMPLATELEVEL` | CHAR(2) | NOT NULL |  |  |  |
| 8 | `SUPPLIERLEVEL` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `DESTINATIONWAREHOUSELEVEL` | CHAR(2) | NOT NULL |  |  |  |
| 10 | `CURRENCYLEVEL` | CHAR(2) | NOT NULL |  |  |  |
| 11 | `PRICELISTLEVEL` | CHAR(2) | NOT NULL |  |  |  |
| 12 | `RRCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 13 | `RRCOUNTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `REPLENISHMENTCUSTOMIZATION.COMPANYCODE = COMPANY.CODE` |
| `COUNTER_RRCOUNTER` | `RRCOUNTERCOMPANYCODE`, `RRCOUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `REPLENISHMENTCUSTOMIZATION.RRCOUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND REPLENISHMENTCUSTOMIZATION.RRCOUNTERCODE = COUNTER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `REPLENISHMENTCUSTOMIZATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONLEVEL,
       t.REQUISITIONTEMPLATELEVEL,
       t.APPLICANTLEVEL,
       t.DELIVERYDATELEVEL,
       t.COSTCENTERLEVEL,
       t.PURCHASEORDERTEMPLATELEVEL,
       t.PURCHASEORDERLINETEMPLATELEVEL,
       t.SUPPLIERLEVEL,
       t.DESTINATIONWAREHOUSELEVEL,
       t.CURRENCYLEVEL,
       t.PRICELISTLEVEL
FROM   DB2ADMIN.REPLENISHMENTCUSTOMIZATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
