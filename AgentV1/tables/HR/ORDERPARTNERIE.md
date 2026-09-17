# DB2ADMIN.ORDERPARTNERIE

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 48
- **Primary key**: `CUSTOMERSUPPLIERCOMPANYCODE`, `CUSTOMERSUPPLIERTYPE`, `CUSTOMERSUPPLIERCODE`
- **FK degree**: referenced by 1 constraint(s), references 7 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 129492

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CUSTOMERSUPPLIERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `CUSTOMERSUPPLIERTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 2 | `CUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `RANGECODE` | CHAR(15) |  |  |  |  |
| 4 | `RANGEDESCRIPTION` | CHAR(100) |  |  |  |  |
| 5 | `RANGEDIVISIONCODE` | CHAR(15) |  |  |  |  |
| 6 | `RANGEDIVISIONDESCRIPTION` | CHAR(100) |  |  |  |  |
| 7 | `COMMISSIONERATE` | CHAR(30) |  |  |  |  |
| 8 | `CEREGISTRATIONNO` | CHAR(30) |  |  |  |  |
| 9 | `CEREGISTRATIONDATE` | DATE |  |  |  |  |
| 10 | `ECCTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 11 | `ECCNO` | CHAR(30) |  |  |  |  |
| 12 | `ECCDATE` | DATE |  |  |  |  |
| 13 | `CSTNO` | CHAR(30) |  |  |  |  |
| 14 | `CSTDATE` | DATE |  |  |  |  |
| 15 | `SSTNO` | CHAR(30) |  |  |  |  |
| 16 | `SSTDATE` | DATE |  |  |  |  |
| 17 | `SALESTAXCODE` | CHAR(30) |  |  |  |  |
| 18 | `SSINUMBER` | CHAR(30) |  |  |  |  |
| 19 | `SSIDATE` | DATE |  |  |  |  |
| 20 | `TAXTEMPLATEHEADERTEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 21 | `TAXTEMPLATEHEADERCODE` | CHAR(3) |  |  |  |  |
| 22 | `TAXTEMPLATEDETAILTEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 23 | `TAXTEMPLATEDETAILCODE` | CHAR(3) |  |  |  |  |
| 24 | `PORTOFDISCHARGECODE` | CHAR(10) |  | FK | foreign_key |  |
| 25 | `PORTOFLOADINGCODE` | CHAR(10) |  | FK | foreign_key |  |
| 26 | `FINALDESTINATIONCODE` | CHAR(3) |  | FK | foreign_key |  |
| 27 | `COUNTRYOFDESTINATIONCODE` | CHAR(3) |  | FK | foreign_key |  |
| 28 | `STATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 29 | `GLCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 30 | `GLCODE` | CHAR(20) |  | FK | foreign_key |  |
| 31 | `INSURANCECHARGES` | DECIMAL(18,5) |  |  |  |  |
| 32 | `FLAG` | CHAR(15) |  |  |  |  |
| 33 | `SAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 34 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 35 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 36 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 37 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 38 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 39 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 40 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 41 | `TYPEOFORDERPARTNER` | CHAR(2) | NOT NULL |  |  |  |
| 42 | `PANNO` | CHAR(10) |  |  |  |  |
| 43 | `TCSAPPLICABILITY` | SMALLINT | NOT NULL |  |  |  |
| 44 | `TDSAPPLICABILITY` | SMALLINT | NOT NULL |  |  |  |
| 45 | `TCSEXEMPTION` | SMALLINT | NOT NULL |  |  |  |
| 46 | `ITRNOTFILED` | SMALLINT | NOT NULL |  |  |  |
| 47 | `MSMENUMBER` | CHAR(30) |  |  |  |  |

## References (this table → parent) — 7

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COUNTRY_COUNTRYOFDESTINATION` | `COUNTRYOFDESTINATIONCODE` | [`COUNTRY`](../CORE_MASTER/COUNTRY.md) | `CODE` | RESTRICT | `ORDERPARTNERIE.COUNTRYOFDESTINATIONCODE = COUNTRY.CODE` |
| `DESTINATION_FINALDESTINATION` | `CUSTOMERSUPPLIERCOMPANYCODE`, `FINALDESTINATIONCODE` | [`DESTINATION`](../CORE_MASTER/DESTINATION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ORDERPARTNERIE.CUSTOMERSUPPLIERCOMPANYCODE = DESTINATION.COMPANYCODE AND ORDERPARTNERIE.FINALDESTINATIONCODE = DESTINATION.CODE` |
| `ECCTYPE_ECCTYPE` | `CUSTOMERSUPPLIERCOMPANYCODE`, `ECCTYPECODE` | [`ECCTYPE`](../HR/ECCTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ORDERPARTNERIE.CUSTOMERSUPPLIERCOMPANYCODE = ECCTYPE.COMPANYCODE AND ORDERPARTNERIE.ECCTYPECODE = ECCTYPE.CODE` |
| `GLMASTER_GL` | `GLCOMPANYCODE`, `GLCODE` | [`GLMASTER`](../CORE_MASTER/GLMASTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ORDERPARTNERIE.GLCOMPANYCODE = GLMASTER.COMPANYCODE AND ORDERPARTNERIE.GLCODE = GLMASTER.CODE` |
| `PORT_PORTOFDISCHARGE` | `PORTOFDISCHARGECODE` | [`PORT`](../CORE_MASTER/PORT.md) | `CODE` | RESTRICT | `ORDERPARTNERIE.PORTOFDISCHARGECODE = PORT.CODE` |
| `PORT_PORTOFLOADING` | `PORTOFLOADINGCODE` | [`PORT`](../CORE_MASTER/PORT.md) | `CODE` | RESTRICT | `ORDERPARTNERIE.PORTOFLOADINGCODE = PORT.CODE` |
| `STATE_STATE` | `STATECODE` | [`STATE`](../HR/STATE.md) | `CODE` | RESTRICT | `ORDERPARTNERIE.STATECODE = STATE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ORDERPARTNERIE_LINE` | [`INSURANCEDETAIL`](../OTHER/INSURANCEDETAIL.md) | `ORDPRNIECSMSUPCOMPANYCODE`, `ORDPRNIECUSTOMERSUPPLIERTYPE`, `ORDPRNIECUSTOMERSUPPLIERCODE` | `INSURANCEDETAIL.ORDPRNIECSMSUPCOMPANYCODE = ORDERPARTNERIE.CUSTOMERSUPPLIERCOMPANYCODE AND INSURANCEDETAIL.ORDPRNIECUSTOMERSUPPLIERTYPE = ORDERPARTNERIE.CUSTOMERSUPPLIERTYPE AND INSURANCEDETAIL.ORDPRNIECUSTOMERSUPPLIERCODE = ORDERPARTNERIE.CUSTOMERSUPPLIERCODE` |

## Indexes

- `ORDERPARTNERIEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CUSTOMERSUPPLIERCOMPANYCODE,
       t.CUSTOMERSUPPLIERTYPE,
       t.CUSTOMERSUPPLIERCODE,
       t.RANGECODE,
       t.RANGEDESCRIPTION,
       t.RANGEDIVISIONCODE,
       t.RANGEDIVISIONDESCRIPTION,
       t.COMMISSIONERATE,
       t.CEREGISTRATIONNO,
       t.CEREGISTRATIONDATE,
       t.ECCTYPECODE,
       t.ECCNO
FROM   DB2ADMIN.ORDERPARTNERIE t
FETCH FIRST 100 ROWS ONLY;
```
