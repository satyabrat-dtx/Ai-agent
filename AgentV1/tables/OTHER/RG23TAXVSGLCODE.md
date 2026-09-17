# DB2ADMIN.RG23TAXVSGLCODE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `COMPANYCODE`, `EVENTCODECODE`, `ITAXCODE`, `INPUTCAPITAL`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 143750

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EVENTCODECODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ITAXCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `INPUTCAPITAL` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `DEBITGLCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `DEBITGLCODE` | CHAR(20) |  | FK | foreign_key |  |
| 6 | `CREDITGLCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `CREDITGLCODE` | CHAR(20) |  | FK | foreign_key |  |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `RG23TAXVSGLCODE.COMPANYCODE = COMPANY.CODE` |
| `EVENTMASTER_EVENTCODE` | `EVENTCODECODE` | [`EVENTMASTER`](../CORE_MASTER/EVENTMASTER.md) | `CODE` | RESTRICT | `RG23TAXVSGLCODE.EVENTCODECODE = EVENTMASTER.CODE` |
| `GLMASTER_CREDITGL` | `CREDITGLCOMPANYCODE`, `CREDITGLCODE` | [`GLMASTER`](../CORE_MASTER/GLMASTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RG23TAXVSGLCODE.CREDITGLCOMPANYCODE = GLMASTER.COMPANYCODE AND RG23TAXVSGLCODE.CREDITGLCODE = GLMASTER.CODE` |
| `GLMASTER_DEBITGL` | `DEBITGLCOMPANYCODE`, `DEBITGLCODE` | [`GLMASTER`](../CORE_MASTER/GLMASTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RG23TAXVSGLCODE.DEBITGLCOMPANYCODE = GLMASTER.COMPANYCODE AND RG23TAXVSGLCODE.DEBITGLCODE = GLMASTER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RG23TAXVSGLCODEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EVENTCODECODE,
       t.ITAXCODE,
       t.INPUTCAPITAL,
       t.DEBITGLCOMPANYCODE,
       t.DEBITGLCODE,
       t.CREDITGLCOMPANYCODE,
       t.CREDITGLCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.RG23TAXVSGLCODE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
