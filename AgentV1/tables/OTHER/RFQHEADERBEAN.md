# DB2ADMIN.RFQHEADERBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 34
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 110512

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `RFQTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 4 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 5 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 6 | `RFQDATE` | DATE |  |  |  |  |
| 7 | `VALIDDAYS` | INTEGER | NOT NULL |  |  |  |
| 8 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 9 | `USERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 10 | `PRODUCTGROUPCODE` | CHAR(10) |  |  |  |  |
| 11 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 12 | `EXCHANGERATE` | DECIMAL(18,5) |  |  |  |  |
| 13 | `DEFAULTCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 14 | `DEFAULTCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 15 | `PROGRESSSTATUS` | CHAR(1) |  |  |  |  |
| 16 | `MANUALCLOSURE` | SMALLINT | NOT NULL |  |  |  |
| 17 | `REMARK` | VARCHAR(1000) |  |  |  |  |
| 18 | `STATUSFLAG` | CHAR(1) |  |  |  |  |
| 19 | `READFLAG` | CHAR(1) |  |  |  |  |
| 20 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 21 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 22 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 23 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 24 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 25 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 26 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 27 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 28 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 29 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 30 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 31 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 32 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 33 | `ADDITIONALDATA` | BLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RFQHEADERBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.RFQTEMPLATECODE,
       t.COUNTERCODE,
       t.CODE,
       t.RFQDATE,
       t.VALIDDAYS,
       t.ITEMTYPECODE,
       t.USERGENERICGROUPTYPECODE,
       t.PRODUCTGROUPCODE,
       t.CURRENCYCODE
FROM   DB2ADMIN.RFQHEADERBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
