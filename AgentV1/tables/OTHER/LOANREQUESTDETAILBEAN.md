# DB2ADMIN.LOANREQUESTDETAILBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 46
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 173567

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DISBURSEMENTAMOUNT` | DECIMAL(11,2) |  |  |  |  |
| 3 | `DISBURSMENTDATE` | DATE |  |  |  |  |
| 4 | `PAYMENTDATE` | DATE |  |  |  |  |
| 5 | `LENGTHOFLOAN` | DECIMAL(3,0) |  |  |  |  |
| 6 | `NOOFINSTALLMENTPERYEAR` | DECIMAL(3,0) |  |  |  |  |
| 7 | `TOTNOOFINSTALLMENTS` | DECIMAL(3,0) |  |  |  |  |
| 8 | `INTERESTRATE` | DECIMAL(5,2) |  |  |  |  |
| 9 | `ADJREQUIRED` | INTEGER | NOT NULL |  |  |  |
| 10 | `ADJLENGTHOFLOAN` | DECIMAL(3,0) |  |  |  |  |
| 11 | `ADJNOOFINSTALLMENTPERYEAR` | DECIMAL(3,0) |  |  |  |  |
| 12 | `ADJTOTNOOFINSTALLMENTS` | DECIMAL(3,0) |  |  |  |  |
| 13 | `ADJINTERESTRATE` | DECIMAL(5,2) |  |  |  |  |
| 14 | `EMI` | DECIMAL(11,2) |  |  |  |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 19 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 20 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 21 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 22 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 23 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 24 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 25 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 26 | `BALANCE` | DECIMAL(11,2) |  |  |  |  |
| 27 | `EMIPENDING` | DECIMAL(11,2) |  |  |  |  |
| 28 | `NETBALANCE` | DECIMAL(11,2) |  |  |  |  |
| 29 | `LOANSTATUS` | INTEGER | NOT NULL |  |  |  |
| 30 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 31 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 32 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 33 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 34 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 35 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 36 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 37 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 38 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 39 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 40 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 41 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 42 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 43 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 44 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 45 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOANREQUEST**.`ABSUNIQUEID` (high confidence — name = 'LOANREQUEST' + known child suffix 'DETAIL')
  - JOIN predicate: `LOANREQUESTDETAILBEAN.FATHERID = LOANREQUEST.ABSUNIQUEID`

## Indexes

- `LOANREQUESTDETAILBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.DISBURSEMENTAMOUNT,
       t.DISBURSMENTDATE,
       t.PAYMENTDATE,
       t.LENGTHOFLOAN,
       t.NOOFINSTALLMENTPERYEAR,
       t.TOTNOOFINSTALLMENTS,
       t.INTERESTRATE,
       t.ADJREQUIRED,
       t.ADJLENGTHOFLOAN,
       t.ADJNOOFINSTALLMENTPERYEAR
FROM   DB2ADMIN.LOANREQUESTDETAILBEAN t
FETCH FIRST 100 ROWS ONLY;
```
