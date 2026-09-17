# DB2ADMIN.ITEMVSEVENTGLMAPBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'ITEM')
- **Roles**: `staging_mirror`
- **Columns**: 50
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 147751

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `EVENTCODE` | CHAR(15) |  |  |  |  |
| 3 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 4 | `MRNPREFIXCODE` | CHAR(3) |  |  |  |  |
| 5 | `INVOICETYPECODE` | CHAR(3) |  |  |  |  |
| 6 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 7 | `USERGENERICGRPCODE` | CHAR(4) |  |  |  |  |
| 8 | `USERGENERICGRPNAMECODE` | CHAR(10) |  |  |  |  |
| 9 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 10 | `STOCKTRANSACTIONTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 11 | `BOOKINGFOR` | CHAR(1) |  |  |  |  |
| 12 | `DOCUMENT` | CHAR(1) |  |  |  |  |
| 13 | `TEMPLATECODE` | CHAR(8) |  |  |  |  |
| 14 | `DEBITGLCODE` | CHAR(20) |  |  |  |  |
| 15 | `CREDITGLCODE` | CHAR(20) |  |  |  |  |
| 16 | `DIFFERENCEGLCODE` | CHAR(20) |  |  |  |  |
| 17 | `EFFECTIVEFROMDATE` | DATE |  |  |  |  |
| 18 | `EFFECTIVETODATE` | DATE |  |  |  |  |
| 19 | `POSTINGFLAG` | INTEGER | NOT NULL |  |  |  |
| 20 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 21 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 22 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 23 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 24 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 25 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 26 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 27 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 28 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 29 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 30 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 31 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 32 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 33 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 34 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 35 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 36 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 37 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 38 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 39 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 40 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 41 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 42 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 43 | `DEMANDTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 44 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 45 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |
| 46 | `COSTDIFFERENCEGLCODE` | CHAR(20) |  |  |  |  |
| 47 | `GROUPBYPROJECT` | SMALLINT | NOT NULL |  |  |  |
| 48 | `PRODUCTIONCOSTVARIANCECODE` | CHAR(20) |  |  |  |  |
| 49 | `COSTINGCALCULATION` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ITEMVSEVENTGLMAPBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.EVENTCODE,
       t.DIVISIONCODE,
       t.MRNPREFIXCODE,
       t.INVOICETYPECODE,
       t.ITEMTYPECODE,
       t.USERGENERICGRPCODE,
       t.USERGENERICGRPNAMECODE,
       t.LOGICALWAREHOUSECODE,
       t.STOCKTRANSACTIONTEMPLATECODE,
       t.BOOKINGFOR
FROM   DB2ADMIN.ITEMVSEVENTGLMAPBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
