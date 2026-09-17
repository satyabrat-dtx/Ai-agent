# DB2ADMIN.DRDETAILSALESDOCUMENT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `COMPANYCODE`, `COUNTERCODE`, `REQUESTCODE`, `LINENR`, `SALDOCSALDOCPRVCOUNTERCODE`, `SALDOCSALDOCPROVISIONALCODE`, `SALESDOCUMENTORDERLINE`, `SALESDOCUMENTORDERSUBLINE`, `SALDOCUMENTCOMPONENTORDERLINE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 214558

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `COUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `REQUESTCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LINENR` | DECIMAL(5,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `SALDOCSALDOCPRVCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 5 | `SALDOCSALDOCPROVISIONALCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 6 | `SALESDOCUMENTORDERLINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 7 | `SALESDOCUMENTORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 8 | `SALDOCUMENTCOMPONENTORDERLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `DEVELOPMENTREQUESTDETAIL_DRDETAILSALESDOCUMENT` | `COMPANYCODE`, `COUNTERCODE`, `REQUESTCODE`, `LINENR` | [`DEVELOPMENTREQUESTDETAIL`](../CORE_MASTER/DEVELOPMENTREQUESTDETAIL.md) | `DEVELOPMENTREQUESTCOMPANYCODE`, `DEVELOPMENTREQUESTCOUNTERCODE`, `DEVELOPMENTREQUESTCODE`, `LINENR` | RESTRICT | `DRDETAILSALESDOCUMENT.COMPANYCODE = DEVELOPMENTREQUESTDETAIL.DEVELOPMENTREQUESTCOMPANYCODE AND DRDETAILSALESDOCUMENT.COUNTERCODE = DEVELOPMENTREQUESTDETAIL.DEVELOPMENTREQUESTCOUNTERCODE AND DRDETAILSALESDOCUMENT.REQUESTCODE = DEVELOPMENTREQUESTDETAIL.DEVELOPMENTREQUESTCODE AND DRDETAILSALESDOCUMENT.LINENR = DEVELOPMENTREQUESTDETAIL.LINENR` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `DRDETAILSALESDOCUMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.COUNTERCODE,
       t.REQUESTCODE,
       t.LINENR,
       t.SALDOCSALDOCPRVCOUNTERCODE,
       t.SALDOCSALDOCPROVISIONALCODE,
       t.SALESDOCUMENTORDERLINE,
       t.SALESDOCUMENTORDERSUBLINE,
       t.SALDOCUMENTCOMPONENTORDERLINE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.DRDETAILSALESDOCUMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
