# DB2ADMIN.SALESPRICEDEFINITIONBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `SALES` (high confidence — table name starts with 'SALES')
- **Roles**: `staging_mirror`
- **Columns**: 71
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 81208

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `NUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 3 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 4 | `INITIALDATE` | DATE |  |  |  |  |
| 5 | `FINALDATE` | DATE |  |  |  |  |
| 6 | `TEMPLATEDEFINITIONTYPE` | CHAR(1) |  |  |  |  |
| 7 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 8 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 9 | `PRICELISTTYPE` | CHAR(2) |  |  |  |  |
| 10 | `COMPOUNDPRICEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 11 | `BREAKDOWNTYPE` | CHAR(2) |  |  |  |  |
| 12 | `UNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 13 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 14 | `PRICEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 15 | `ORDERTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 16 | `AREACODE` | CHAR(3) |  |  |  |  |
| 17 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 18 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 19 | `AGENTCODE` | CHAR(3) |  |  |  |  |
| 20 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 21 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 22 | `ORDERPARTNERBRANDCODE` | CHAR(8) |  |  |  |  |
| 23 | `FNCORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 24 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 25 | `ORDPRNGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 26 | `ORDERPARTNERGROUPCODE` | CHAR(3) |  |  |  |  |
| 27 | `LINEUSERVALUE` | CHAR(20) |  |  |  |  |
| 28 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 29 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 30 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 31 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 33 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 34 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 35 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 36 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 37 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 38 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 39 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 40 | `ORDITEMGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 41 | `ORDERITEMGROUPCODE` | CHAR(3) |  |  |  |  |
| 42 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 43 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 44 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 45 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 46 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 47 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 48 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 49 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 50 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 51 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 52 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 53 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 54 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 55 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 56 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 57 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 58 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 59 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 60 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 61 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 62 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 63 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 64 | `RFPARTNERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 65 | `RFPRNGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 66 | `REFERENCEPARTNERGROUPCODE` | CHAR(3) |  |  |  |  |
| 67 | `PROTOTYPEMANAGED` | SMALLINT | NOT NULL |  |  |  |
| 68 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 69 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 70 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESPRICEDEFINITIONBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.NUMBERID,
       t.ORDERTYPE,
       t.INITIALDATE,
       t.FINALDATE,
       t.TEMPLATEDEFINITIONTYPE,
       t.TEMPLATECODE,
       t.PRICELISTCODE,
       t.PRICELISTTYPE,
       t.COMPOUNDPRICEREQUIRED,
       t.BREAKDOWNTYPE
FROM   DB2ADMIN.SALESPRICEDEFINITIONBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
