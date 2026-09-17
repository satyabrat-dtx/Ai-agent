# DB2ADMIN.PAYMENTMETHODIBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 90
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 201162

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 4 | `CODE` | CHAR(3) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `PAYMENTVARIANT` | CHAR(1) |  |  |  |  |
| 6 | `NOOFDAYS` | INTEGER | NOT NULL |  |  |  |
| 7 | `NOOFDAYS1` | INTEGER | NOT NULL |  |  |  |
| 8 | `NOOFDAYS2` | INTEGER | NOT NULL |  |  |  |
| 9 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 10 | `PAYMENTWITHBILLS` | SMALLINT | NOT NULL |  |  |  |
| 11 | `INITIALDATE` | DATE |  |  |  |  |
| 12 | `FINALDATE` | DATE |  |  |  |  |
| 13 | `INACTIVE` | SMALLINT | NOT NULL |  |  |  |
| 14 | `DUEDATEEXCEPTIONCODE` | CHAR(6) |  |  |  |  |
| 15 | `PERCENTAGE1` | DECIMAL(9,5) |  |  |  |  |
| 16 | `PERCENTAGE2` | DECIMAL(9,5) |  |  |  |  |
| 17 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 18 | `FLAG` | CHAR(12) |  |  |  |  |
| 19 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 20 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 21 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 22 | `DISCOUNTDAYS1` | INTEGER | NOT NULL |  |  |  |
| 23 | `DISCOUNTRATE1` | DECIMAL(5,2) |  |  |  |  |
| 24 | `FIXEDDAY1` | INTEGER | NOT NULL |  |  |  |
| 25 | `MONTH1` | INTEGER | NOT NULL |  |  |  |
| 26 | `DISCOUNTDAYS2` | INTEGER | NOT NULL |  |  |  |
| 27 | `DISCOUNTRATE2` | DECIMAL(5,2) |  |  |  |  |
| 28 | `FIXEDDAY2` | INTEGER | NOT NULL |  |  |  |
| 29 | `MONTH2` | INTEGER | NOT NULL |  |  |  |
| 30 | `DISCOUNTDAYS3` | INTEGER | NOT NULL |  |  |  |
| 31 | `DISCOUNTRATE3` | DECIMAL(5,2) |  |  |  |  |
| 32 | `FIXEDDAY3` | INTEGER | NOT NULL |  |  |  |
| 33 | `MONTH3` | INTEGER | NOT NULL |  |  |  |
| 34 | `NETDAYS` | INTEGER | NOT NULL |  |  |  |
| 35 | `FIXEDDAYNET` | INTEGER | NOT NULL |  |  |  |
| 36 | `NETMONTH` | INTEGER | NOT NULL |  |  |  |
| 37 | `TOLERANCEDAYS` | INTEGER | NOT NULL |  |  |  |
| 38 | `SPLITSTART` | CHAR(1) |  |  |  |  |
| 39 | `SPLITMONTHRULE` | CHAR(3) |  |  |  |  |
| 40 | `SPLITFIXDAY1` | INTEGER | NOT NULL |  |  |  |
| 41 | `SPLITFIXDAY2` | INTEGER | NOT NULL |  |  |  |
| 42 | `SPLITFIXDAY3` | INTEGER | NOT NULL |  |  |  |
| 43 | `SPLITFIXDAY4` | INTEGER | NOT NULL |  |  |  |
| 44 | `SPLITFIXDAY5` | INTEGER | NOT NULL |  |  |  |
| 45 | `SPLITDAYS1` | INTEGER | NOT NULL |  |  |  |
| 46 | `SPLITSHARE1` | INTEGER | NOT NULL |  |  |  |
| 47 | `SPLITSHARECALC1` | DECIMAL(5,2) |  |  |  |  |
| 48 | `SPLITDAYS2` | INTEGER | NOT NULL |  |  |  |
| 49 | `SPLITSHARE2` | INTEGER | NOT NULL |  |  |  |
| 50 | `SPLITSHARECALC2` | DECIMAL(5,2) |  |  |  |  |
| 51 | `SPLITDAYS3` | INTEGER | NOT NULL |  |  |  |
| 52 | `SPLITSHARE3` | INTEGER | NOT NULL |  |  |  |
| 53 | `SPLITSHARECALC3` | DECIMAL(5,2) |  |  |  |  |
| 54 | `SPLITDAYS4` | INTEGER | NOT NULL |  |  |  |
| 55 | `SPLITSHARE4` | INTEGER | NOT NULL |  |  |  |
| 56 | `SPLITSHARECALC4` | DECIMAL(5,2) |  |  |  |  |
| 57 | `SPLITDAYS5` | INTEGER | NOT NULL |  |  |  |
| 58 | `SPLITSHARE5` | INTEGER | NOT NULL |  |  |  |
| 59 | `SPLITSHARECALC5` | DECIMAL(5,2) |  |  |  |  |
| 60 | `SPLITDAYS6` | INTEGER | NOT NULL |  |  |  |
| 61 | `SPLITSHARE6` | INTEGER | NOT NULL |  |  |  |
| 62 | `SPLITSHARECALC6` | DECIMAL(5,2) |  |  |  |  |
| 63 | `SPLITEXPIREDATERULE1` | CHAR(1) |  |  |  |  |
| 64 | `SPLITEXPIREDATERULE2` | CHAR(1) |  |  |  |  |
| 65 | `SPLITEXPIREDATERULE3` | CHAR(1) |  |  |  |  |
| 66 | `SPLITEXPIREDATERULE4` | CHAR(1) |  |  |  |  |
| 67 | `SPLITEXPIREDATERULE5` | CHAR(1) |  |  |  |  |
| 68 | `SPLITEXPIREDATERULE6` | CHAR(1) |  |  |  |  |
| 69 | `SPLITPAYMENTTYPE1CODE` | CHAR(3) |  |  |  |  |
| 70 | `SPLITPAYMENTTYPE2CODE` | CHAR(3) |  |  |  |  |
| 71 | `SPLITPAYMENTTYPE3CODE` | CHAR(3) |  |  |  |  |
| 72 | `SPLITPAYMENTTYPE4CODE` | CHAR(3) |  |  |  |  |
| 73 | `SPLITPAYMENTTYPE5CODE` | CHAR(3) |  |  |  |  |
| 74 | `SPLITPAYMENTTYPE6CODE` | CHAR(3) |  |  |  |  |
| 75 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 76 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 77 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 78 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 79 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 80 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 81 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 82 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 83 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 84 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 85 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 86 | `FINLABELS` | CHAR(1) |  |  |  |  |
| 87 | `COLLECTIONMODE` | CHAR(1) |  |  |  |  |
| 88 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 89 | `EIPAYMENTTYPECODE` | CHAR(4) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PAYMENTMETHODIBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.CODE,
       t.PAYMENTVARIANT,
       t.NOOFDAYS,
       t.NOOFDAYS1,
       t.NOOFDAYS2,
       t.LONGDESCRIPTION,
       t.PAYMENTWITHBILLS,
       t.INITIALDATE
FROM   DB2ADMIN.PAYMENTMETHODIBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
