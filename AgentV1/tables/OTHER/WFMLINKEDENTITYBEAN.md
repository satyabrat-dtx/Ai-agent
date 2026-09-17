# DB2ADMIN.WFMLINKEDENTITYBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 33
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 108342

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `GROUPFAMILY` | CHAR(15) |  |  |  |  |
| 2 | `REFERENCEDENTITY` | CHAR(50) |  |  |  |  |
| 3 | `REFERENCEDENTITYPK` | CHAR(140) |  |  |  |  |
| 4 | `REFERENCEDENTITYGROUP` | CHAR(140) |  |  |  |  |
| 5 | `WFMPROCESSID` | CHAR(120) |  |  |  |  |
| 6 | `WFMPROCESSKEY` | CHAR(50) |  |  |  |  |
| 7 | `UIXMLPATH` | VARCHAR(50) |  |  |  |  |
| 8 | `UIXMLNAME` | VARCHAR(54) |  |  |  |  |
| 9 | `PISTATUS` | INTEGER | NOT NULL |  |  |  |
| 10 | `REASONCODE` | CHAR(50) |  |  |  |  |
| 11 | `REMARK` | CLOB(2000000) |  |  |  |  |
| 12 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 13 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 14 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 15 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 16 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 17 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 18 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 19 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 20 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 21 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 22 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 23 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 24 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 25 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 26 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 27 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 28 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 29 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 30 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 31 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 32 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WFMLINKEDENTITYBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.GROUPFAMILY,
       t.REFERENCEDENTITY,
       t.REFERENCEDENTITYPK,
       t.REFERENCEDENTITYGROUP,
       t.WFMPROCESSID,
       t.WFMPROCESSKEY,
       t.UIXMLPATH,
       t.UIXMLNAME,
       t.PISTATUS,
       t.REASONCODE,
       t.REMARK
FROM   DB2ADMIN.WFMLINKEDENTITYBEAN t
FETCH FIRST 100 ROWS ONLY;
```
