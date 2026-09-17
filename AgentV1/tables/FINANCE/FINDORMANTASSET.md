# DB2ADMIN.FINDORMANTASSET

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `COMPANYCODE`, `ASSETNUMBERCOUNTERCODE`, `ASSETNUMBERCODE`, `FINANCIALYEARCODE`, `FROMDATE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 175809

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ASSETNUMBERCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `ASSETNUMBERCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 3 | `FINANCIALYEARCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 4 | `FINANCIALYEARCODE` | DECIMAL(4,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `FROMDATE` | DATE | NOT NULL | PK | primary_key | Inclusive start of a validity period. |
| 6 | `TODATE` | DATE | NOT NULL |  |  | End of a validity period. |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FINFINANCIALYEAR_FINANCIALYEAR` | `FINANCIALYEARCOMPANYCODE`, `FINANCIALYEARCODE` | [`FINFINANCIALYEAR`](../FINANCE/FINFINANCIALYEAR.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINDORMANTASSET.FINANCIALYEARCOMPANYCODE = FINFINANCIALYEAR.COMPANYCODE AND FINDORMANTASSET.FINANCIALYEARCODE = FINFINANCIALYEAR.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINDORMANTASSETUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ASSETNUMBERCOUNTERCODE,
       t.ASSETNUMBERCODE,
       t.FINANCIALYEARCOMPANYCODE,
       t.FINANCIALYEARCODE,
       t.FROMDATE,
       t.TODATE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.FINDORMANTASSET t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
