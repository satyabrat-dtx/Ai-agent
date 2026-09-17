# DB2ADMIN.FINNEGOTIATIONSUBVENTIONENTRY

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `FINEXPNEGOTIATIONCOMPANYCODE`, `FINEXPNEGOTIATIONCODE`, `INTERESTGLCODE`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 201846

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINEXPNEGOTIATIONCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FINEXPNEGOTIATIONCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `INTERESTRATE` | DECIMAL(5,2) |  |  |  |  |
| 3 | `INTERESTGLCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 4 | `INTERESTGLCODE` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `INTERESTAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 6 | `POSTINGDATE` | DATE |  |  |  |  |
| 7 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 8 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 9 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 10 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 11 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 12 | `REMARK` | VARCHAR(255) |  |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FINEXPNEGOTIATION_SUBVENTION` | `FINEXPNEGOTIATIONCOMPANYCODE`, `FINEXPNEGOTIATIONCODE` | [`FINEXPNEGOTIATION`](../FINANCE/FINEXPNEGOTIATION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINNEGOTIATIONSUBVENTIONENTRY.FINEXPNEGOTIATIONCOMPANYCODE = FINEXPNEGOTIATION.COMPANYCODE AND FINNEGOTIATIONSUBVENTIONENTRY.FINEXPNEGOTIATIONCODE = FINEXPNEGOTIATION.CODE` |
| `GLMASTER_INTERESTGL` | `INTERESTGLCOMPANYCODE`, `INTERESTGLCODE` | [`GLMASTER`](../CORE_MASTER/GLMASTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINNEGOTIATIONSUBVENTIONENTRY.INTERESTGLCOMPANYCODE = GLMASTER.COMPANYCODE AND FINNEGOTIATIONSUBVENTIONENTRY.INTERESTGLCODE = GLMASTER.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `FINNEGOTIATIONSUBVENTIONENTRY_NS` | [`FINDOCUMENT`](../FINANCE/FINDOCUMENT.md) | `COMPANYCODE`, `NSFINEXPNEGOTIATIONCODE`, `NSINTERESTGLCODE` | `FINDOCUMENT.COMPANYCODE = FINNEGOTIATIONSUBVENTIONENTRY.FINEXPNEGOTIATIONCOMPANYCODE AND FINDOCUMENT.NSFINEXPNEGOTIATIONCODE = FINNEGOTIATIONSUBVENTIONENTRY.FINEXPNEGOTIATIONCODE AND FINDOCUMENT.NSINTERESTGLCODE = FINNEGOTIATIONSUBVENTIONENTRY.INTERESTGLCODE` |

## Indexes

- `FINNSUBVENTIONENTRYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FINEXPNEGOTIATIONCOMPANYCODE,
       t.FINEXPNEGOTIATIONCODE,
       t.INTERESTRATE,
       t.INTERESTGLCOMPANYCODE,
       t.INTERESTGLCODE,
       t.INTERESTAMOUNT,
       t.POSTINGDATE,
       t.FINDOCBUSINESSUNITCODE,
       t.FINDOCFINANCIALYEARCODE,
       t.FINDOCTEMPLATECODE,
       t.FINDOCSTATISTICALGROUPCODE,
       t.FINDOCCODE
FROM   DB2ADMIN.FINNEGOTIATIONSUBVENTIONENTRY t
FETCH FIRST 100 ROWS ONLY;
```
