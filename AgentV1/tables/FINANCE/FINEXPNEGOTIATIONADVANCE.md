# DB2ADMIN.FINEXPNEGOTIATIONADVANCE

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`, `NEGOTIATIONCODE`, `ADVANCECODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 176670

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `NEGOTIATIONCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `ADVANCECODE` | CHAR(5) | NOT NULL | PK | primary_key |  |
| 3 | `BANKGLCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 4 | `BANKGLCODE` | CHAR(20) |  | FK | foreign_key |  |
| 5 | `BANKREFNO` | CHAR(30) |  |  |  |  |
| 6 | `BANKREFDATE` | DATE |  |  |  |  |
| 7 | `ADJUSTEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 8 | `AVERAGERATE` | DECIMAL(18,5) |  |  |  |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `GLMASTER_BANKGL` | `BANKGLCOMPANYCODE`, `BANKGLCODE` | [`GLMASTER`](../CORE_MASTER/GLMASTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINEXPNEGOTIATIONADVANCE.BANKGLCOMPANYCODE = GLMASTER.COMPANYCODE AND FINEXPNEGOTIATIONADVANCE.BANKGLCODE = GLMASTER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINEXPNEGOTIATIONADVANCEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.NEGOTIATIONCODE,
       t.COMPANYCODE,
       t.ADVANCECODE,
       t.BANKGLCOMPANYCODE,
       t.BANKGLCODE,
       t.BANKREFNO,
       t.BANKREFDATE,
       t.ADJUSTEDAMOUNT,
       t.AVERAGERATE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.FINEXPNEGOTIATIONADVANCE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
