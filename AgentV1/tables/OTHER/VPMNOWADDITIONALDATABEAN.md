# DB2ADMIN.VPMNOWADDITIONALDATABEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 33
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 121066

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `NAME` | VARCHAR(120) |  |  |  |  |
| 2 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 3 | `MAXLENGTH` | INTEGER | NOT NULL |  |  |  |
| 4 | `ADNAME` | CHAR(50) |  |  |  |  |
| 5 | `OBJLABEL` | VARCHAR(150) |  |  |  |  |
| 6 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 7 | `LSTLABEL` | VARCHAR(150) |  |  |  |  |
| 8 | `LABEL` | CHAR(50) |  |  |  |  |
| 9 | `HTMLSIZE` | INTEGER | NOT NULL |  |  |  |
| 10 | `READONLY` | INTEGER | NOT NULL |  |  |  |
| 11 | `HTMLTYPE` | CHAR(20) |  |  |  |  |
| 12 | `OPTIONS` | VARCHAR(100) |  |  |  |  |
| 13 | `EDITMASK` | CHAR(50) |  |  |  |  |
| 14 | `TYPE` | CHAR(20) |  |  |  |  |
| 15 | `FIELDTYPE` | INTEGER | NOT NULL |  |  |  |
| 16 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 17 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 18 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 19 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 20 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 21 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 22 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 23 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 24 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 25 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 26 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 27 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 28 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 29 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 30 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 31 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 32 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `VPMNOWADDITIONALDATABEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.NAME,
       t.ENTITYNAME,
       t.MAXLENGTH,
       t.ADNAME,
       t.OBJLABEL,
       t.SEQUENCE,
       t.LSTLABEL,
       t.LABEL,
       t.HTMLSIZE,
       t.READONLY,
       t.HTMLTYPE
FROM   DB2ADMIN.VPMNOWADDITIONALDATABEAN t
FETCH FIRST 100 ROWS ONLY;
```
