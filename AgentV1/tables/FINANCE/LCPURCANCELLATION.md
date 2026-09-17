# DB2ADMIN.LCPURCANCELLATION

- **Module**: `FINANCE` (low confidence — FK neighbourhood: 1 of 1 related tables are FINANCE)
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `LCDETAILPURCOMPANYCODE`, `LCDETAILPURDIVISIONCODE`, `LCDETAILPURLCNO`, `LCDETAILPURLCDATE`, `LINENUMBER`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 218917

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `LCDETAILPURCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `LCDETAILPURDIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LCDETAILPURLCNO` | CHAR(35) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LCDETAILPURLCDATE` | DATE | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `LINENUMBER` | DECIMAL(18,5) | NOT NULL | PK | primary_key |  |
| 5 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 6 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 7 | `CANCELLATIONDATE` | DATE |  |  |  |  |
| 8 | `CANCELLATIONAMT` | DECIMAL(18,5) |  |  |  |  |
| 9 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 10 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 11 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 12 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 13 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 18 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 19 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `LCDETAILPUR_LCPURCANCELLATION` | `LCDETAILPURCOMPANYCODE`, `LCDETAILPURDIVISIONCODE`, `LCDETAILPURLCNO`, `LCDETAILPURLCDATE` | [`LCDETAILPUR`](../FINANCE/LCDETAILPUR.md) | `COMPANYCODE`, `DIVISIONCODE`, `LCNO`, `LCDATE` | RESTRICT | `LCPURCANCELLATION.LCDETAILPURCOMPANYCODE = LCDETAILPUR.COMPANYCODE AND LCPURCANCELLATION.LCDETAILPURDIVISIONCODE = LCDETAILPUR.DIVISIONCODE AND LCPURCANCELLATION.LCDETAILPURLCNO = LCDETAILPUR.LCNO AND LCPURCANCELLATION.LCDETAILPURLCDATE = LCDETAILPUR.LCDATE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LCPURCANCELLATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.LCDETAILPURCOMPANYCODE,
       t.LCDETAILPURDIVISIONCODE,
       t.LCDETAILPURLCNO,
       t.LCDETAILPURLCDATE,
       t.LINENUMBER,
       t.TAXTEMPLATETEMPLATETYPE,
       t.TAXTEMPLATECODE,
       t.CANCELLATIONDATE,
       t.CANCELLATIONAMT,
       t.FINDOCBUSINESSUNITCODE,
       t.FINDOCFINANCIALYEARCODE,
       t.FINDOCTEMPLATECODE
FROM   DB2ADMIN.LCPURCANCELLATION t
FETCH FIRST 100 ROWS ONLY;
```
